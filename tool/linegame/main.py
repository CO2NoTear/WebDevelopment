import env
import numpy as np
import sys
import torch
import torch.nn as nn
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import agent
import matplotlib.pyplot as plt
from agent import DQN
from agent import Flatten
action_choices = []
action = [0,0,0,0]
strategy = True
for i in range(7):
    for j in range(4):
        action_choices.append([j, i, j + 1, i])
for i in range(5):
    for j in range(6):
        action_choices.append([i, j, i, j + 1])
epoisides = int(10000)
reward = 0
cuda = torch.cuda.is_available()
if cuda is True:
    print('===> Using GPU to train')
    os.environ['CUDA_VISIBLE_DEVICES'] = '1'
    device = torch.device('cuda')

else:
    print('===> Using CPU to train')
    device = torch.device('cpu')
red = DQN(140, action_choices, "red")
blue = DQN(140, action_choices, "blue")
scores_red = []
scores_blue = []
flatten = nn.Sequential(Flatten(),
                        Flatten()
                        )
if(os.path.exists('red.pth')):
    state_dict = torch.load('red.pth')
    red.train_net.load_state_dict(state_dict)
    red.target_net.load_state_dict(red.train_net.state_dict())
if(os.path.exists('blue.pth')):
    state_dict = torch.load('blue.pth')
    blue.train_net.load_state_dict(state_dict)
    blue.target_net.load_state_dict(blue.train_net.state_dict())
for epoiside in range(epoisides):
    if((epoiside + 1) % 100 == 0):
        strategy = not strategy
    game = env.LineGame()
    while(not game.terminal):
        #game.show()
        #act_show = []
        #for i in range(4):
        #    act_show.append(action[i] + 1)
        #print(f"last reward: {reward}. player's role: {game.role}, {game.cnt} places have been taken")
        #print(f"last action is {act_show}")
        #action = []
        s = torch.tensor(game.board,dtype = torch.float32)
        s = flatten(s).to(device)
        if game.role == "red":
            index,action = red.act(s)
            __,reward = game.update(action)
            s_ = flatten(torch.tensor(game.board,dtype = torch.float32)).to(device)
            red.store(s, index, reward, s_)
            if(strategy):
                red.update()
        elif game.role == "blue":
            index,action = blue.act(s)
            __,reward = game.update(action)
            s_ = flatten(torch.tensor(game.board,dtype = torch.float32)).to(device)
            blue.store(s, index, reward, s_)
            if(not strategy):
                blue.update()
        #os.system("pause")
        #os.system("cls")
    s = s_ = torch.tensor(game.board,dtype = torch.float32).to(device)
    s = s_ = flatten(s)
    index_a, action_a = red.act(s)
    index_b, action_b = red.act(s)
    red_, blue_, reward_a, reward_b = game.update(action)
    red.store(s, index_a, reward_a, s_)
    if(strategy):
        red.update()
    blue.store(s, index_b, reward_b, s_)
    if(not strategy):
        blue.update()
    print(f"the game ends,red gets {red_}, blue gets {blue_}")
    scores_red.append(red_)
    scores_blue.append(blue_)
    if((epoiside + 1) % 100 == 0):
        plt.clf()
        x = np.linspace(epoiside - 98,epoiside + 1,num = 100,dtype = int)
        plt.plot(x,np.asarray(scores_red,dtype = int),color='red',linewidth=1.0,linestyle='-')#以x为横坐标，origin为纵坐标，建立曲线图
        #plt.plot(x,np.asarray(scores_blue,dtype = int),color='blue',linewidth=1.0,linestyle='--')
        plt.xlabel('epoiside')
        plt.ylabel('score')
        name = "output/" + str(epoiside + 1) + "red.jpg"
        plt.savefig(name)
        plt.clf()
        plt.plot(x,np.asarray(scores_blue,dtype = int),color='blue',linewidth=1.0,linestyle='--')
        plt.xlabel('epoiside')
        plt.ylabel('score')
        name = "output/" + str(epoiside + 1) + "blue.jpg"
        plt.savefig(name)
        scores_red = []
        scores_blue = []