import numpy as np
a = np.zeros([4,5,7])#创建5个4 * 4的二维数组
a[1][2][0] = -1#下标为1的数组的下标为2行的下标为0列
for i in range(5):
    print(i)
key = {"red" : 1, "blue" : -1}
print(key["red"])
if(not False):
    print(21 == 21)
else:
    print(0)
import torch
a = torch.tensor([1,2,3],dtype = int)
b = torch.tensor([1,2,3],dtype = int)
c = a * b
d = torch.argmax(c)
c = [1,4,9]
print(c)
print(c[d])
e = "asd"
f = ".t7"
g = e + ".t7"
print(g)
h = [a,b,c]
a = torch.tensor([[2,4,7],[3,4,7]])
b = torch.tensor([[1,0,0],[0,1,0]])
c = torch.tensor([[1],[1]])
print(c)
d = (a + c) * b
print(d)
action_choices = []
for i in range(7):
    for j in range(4):
        action_choices.append([j, i, j + 1, i])
for i in range(5):
    for j in range(6):
        action_choices.append([i, j, i, j + 1])
print(action_choices)
x = np.linspace(0,999,1000,dtype = int)#相当于采样点
x = x + 1
print(x)