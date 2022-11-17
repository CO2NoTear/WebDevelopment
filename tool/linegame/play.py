import env
import numpy as np
import sys
import torch
import torch.nn as nn
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import agent
from agent import DQN
from agent import Flatten
action_choices = []
action = [0,0,0,0]
for i in range(7):
    for j in range(4):
        action_choices.append([j, i, j + 1, i])
for i in range(5):
    for j in range(6):
        action_choices.append([i, j, i, j + 1])
epoisides = int(1000)
reward = 0
red = DQN(140, action_choices, "red")
flatten = nn.Sequential(Flatten(),
                        Flatten()
                        )
cuda = torch.cuda.is_available()
if cuda is True:
    print('===> Using GPU to train')
    os.environ['CUDA_VISIBLE_DEVICES'] = '1'
    device = torch.device('cuda')

else:
    print('===> Using CPU to train')
    device = torch.device('cpu')
state_dict = torch.load('red.pth')
red.train_net.load_state_dict(state_dict)
red.target_net.load_state_dict(red.train_net.state_dict())
#red.learn = False
for epoiside in range(epoisides):
    game = env.LineGame()
    while(not game.terminal):
        game.show()
        act_show = []
        for i in range(4):
            act_show.append(action[i] + 1)
        print(f"last reward: {reward}. player's role: {game.role}, {game.cnt} places have been taken")
        print(f"last action is {act_show}")
        action = []
        #action = []
        #for i in range(4):
        #    if i % 2 == 0:
        #        action.append(int(input("please enter " + str(int((i / 2) + 1)) + "_x: ")) - 1)
        #    elif i % 2 == 1:
        #        action.append(int(input("please enter " + str(int((i / 2) + 1)) + "_y: ")) - 1)
        #action = np.asarray(action,dtype = int)
        if game.role == "red":
            s = torch.tensor(game.board,dtype = torch.float32).to(device)
            s = flatten(s)
            index,action = red.act(s)
            __,reward = game.update(action)
            s_ = flatten(torch.tensor(game.board,dtype = torch.float32)).to(device)
            red.store(s, index, reward, s_)
            red.update()
        elif game.role == "blue":
            action = []
            for i in range(4):
                if i % 2 == 0:
                    action.append(int(input("please enter " + str(int((i / 2) + 1)) + "_x: ")) - 1)
                elif i % 2 == 1:
                    action.append(int(input("please enter " + str(int((i / 2) + 1)) + "_y: ")) - 1)
            action = np.asarray(action,dtype = int)
            __,reward = game.update(action)
        os.system("cls")
    s = s_ = torch.tensor(game.board,dtype = torch.float32).to(device)
    s = s_ = flatten(s)
    index_a, action_a = red.act(s)
    red_, blue_, reward_a, reward_b = game.update(action)
    red.store(s, index_a, reward_a, s_)
    red.update()
    print(f"the game ends,red gets {red_}, blue gets {blue_}\n")
print(red_)
print(blue_)