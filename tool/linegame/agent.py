import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy
import os
import random
cuda = torch.cuda.is_available()
if cuda is True:
    print('===> Using GPU to train')
    os.environ['CUDA_VISIBLE_DEVICES'] = '1'
    device = torch.device('cuda')

else:
    print('===> Using CPU to train')
    device = torch.device('cpu')
class Flatten(nn.Module):
    def forward(self, input):
        return input.view(-1)
class NET(nn.Module):
    def __init__(self, state_size, action_choices, **kwargs):
        super(NET, self).__init__(**kwargs)
        self.net = nn.Sequential(
            nn.Linear(state_size, 256),
            nn.Linear(256, 512),
            nn.LeakyReLU(),
            nn.Linear(512, 1024),
            nn.Linear(1024, 2048),
            nn.LeakyReLU(),
            nn.Linear(2048, 2048),
            nn.Linear(2048, 1024),
            nn.LeakyReLU(),
            nn.Linear(1024, 512),
            nn.Linear(512, action_choices)
            )
    def forward(self, state):
        result = self.net(state)
        return result
class DQN():
    def __init__(self, state_size, action_choices, name, *args, **kwargs):
        self.train_net = NET(state_size, 58).to(device)
        self.target_net = NET(state_size, 58).to(device)
        self.target_net.load_state_dict(self.train_net.state_dict())
        self.greedy = 0.1
        self.action_choices = action_choices
        self.choices_number = len(action_choices)
        self.buffer = []
        self.buffer_size = int(1000)
        self.buffer_step = int(0)
        self.lr = 0.4
        self.Gamma = 0.5
        self.step = 0
        self.learn = True
        self.step_size = 50
        self.optimizer = torch.optim.Adam(self.train_net.parameters(), lr = self.lr, weight_decay = 10)
        self.name = name + ".pth"
    def act(self, state):
        if self.learn:
            x = random.random()
            if x < 1 - self.greedy:
                result = self.train_net(state)
                index = torch.argmax(result)
            else:
                index = random.randint(0, self.choices_number - 1)
            action = self.action_choices[index]
            return index, action
        else:
            result = self.train_net(state)
            index = torch.argmax(result)
            action = self.action_choices[index]
            return index, action
    def store(self,s,a,r,s_):
        if len(self.buffer) != self.buffer_size:
            self.buffer.append([s,a,r,s_])
            self.buffer_step += 1
        else:
            self.buffer[self.buffer_step % self.buffer_size] = [s,a,r,s_]
            self.buffer_step += 1
    def update(self):
        self.step += 1
        criterion = nn.MSELoss()
        if self.step % 5 == 0:
            for i in range(50):
                memory = random.choice(self.buffer)
                temp = torch.zeros(58)
                temp = temp.to(device)
                temp[memory[1]] = 1
                q = self.train_net(memory[0]) * temp
                q_ = self.target_net(memory[3])
                temp = torch.zeros(58)
                temp = temp.to(device)
                temp[torch.argmax(q_)] = 1
                q_ = (self.Gamma * q_ + memory[2]) * temp
                if i == 0:
                    loss = criterion(q_ , q)
                else:
                    loss += criterion(q_ , q)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        if self.step % 50 == 0:
            self.target_net.load_state_dict(self.train_net.state_dict())
            torch.save(self.target_net.state_dict(),self.name)
        
