import numpy as np
class LineGame:
    def __init__(self, *args, **kwargs):
        self.board = np.zeros([4,5,7])#have 5 * 7 nodes, for better train an agent, we widen the dimension, 0 - left, 1 - right, 2 - up, 3 -down
        self.showboard = np.zeros([4,6])#show on the screen is 4 * 6 table
        self.mode = ""
        self.role = "red"#"red"/"blue"
        self.cnt = 0;
        self.terminal = False
        self.key = {"red" : 1, "blue" : -1}
        self.reward = 0
    def update(self, action):
        #action[0] - 1_x, action[1] - 1_y, action[2] - 2_x, action[3] - 3_x
        self.reward = 0
        if(not self.terminal):
            if((action[0] < 0 or action[0] >= 5) or (action[2] < 0 or action[2] >= 5) or (action[1] < 0 or action[1] >= 7) or (action[3] < 0 or action[3] >= 7)):
                self.reward = -200
                return "out of range",self.reward
            x = action[0] - action[2];
            y = action[1] - action[3];
            if (x != 0 and y != 0) or (abs(x) > 1) or (abs(y) > 1):
                self.reward = -200
                return "can't draw a line",self.reward
            elif y != 0 and x == 0:
                if y > 0 :#first turn to list_left
                    if((self.board[0][action[0]][action[1]] != 0) and (self.board[1][action[2]][action[3]] != 0)):
                        self.reward = -200
                        return "already done, choose again",self.reward
                    self.board[0][action[0]][action[1]] = 1
                    self.board[1][action[2]][action[3]] = 1
                if y < 0:#first turn to list_right
                    if((self.board[1][action[0]][action[1]] != 0) and (self.board[0][action[2]][action[3]] != 0)):
                        self.reward = -200
                        return "already done, choose again",self.reward
                    self.board[1][action[0]][action[1]] = 1
                    self.board[0][action[2]][action[3]] = 1
            elif x != 0 and y == 0:
                if x < 0:#first turn to list_down
                    if((self.board[3][action[0]][action[1]] != 0) and (self.board[2][action[2]][action[3]] != 0)):
                        self.reward = -200
                        return "already done, choose again",self.reward
                    self.board[3][action[0]][action[1]] = 1
                    self.board[2][action[2]][action[3]] = 1
                if x > 0:#first turn to list_up
                    if((self.board[2][action[0]][action[1]] != 0) and (self.board[3][action[2]][action[3]] != 0)):
                        self.reward = -200
                        return "already done, choose again",self.reward
                    self.board[2][action[0]][action[1]] = 1
                    self.board[3][action[2]][action[3]] = 1
            else:
                self.reward = -200
                return "two points are the same",self.reward
            self.judge()
            return "choice has been made",self.reward
        else:
            red = 0
            blue = 0
            r_a = 0
            r_b = 0
            for i in range(4):
                for j in range(6):
                    if self.showboard[i][j] == 1:
                        red += 1
                    elif self.showboard[i][j] == -1:
                        blue += 1
            if red > blue:
                r_a = 1000
                r_b = -1000
            elif red == blue:
                r_a = 50
                r_b = 50
            elif blue > red:
                r_a = -1000
                r_b = 1000
            return red, blue, r_a, r_b
    def judge(self):
        cnt = 0;
        for i in range(4):
            for j in range(6):
                if self.showboard[i][j] != 0:
                    continue
                else:
                    if ((self.board[3][i][j] != 0) and  (self.board[1][i + 1][j] != 0) and (self.board[2][i + 1][j + 1] != 0) and (self.board[0][i][j + 1] != 0)):
                       self.showboard[i][j] =  self.key[self.role]
                       cnt += 1
                       self.reward += 50
        self.cnt = self.cnt + cnt;
        if cnt == 0:
            if self.role == "red":
                self.role = "blue"
            elif self.role == "blue":
                self.role = "red"
        if self.cnt == 24:
            self.terminal = True
            return "Game End"
        return "Next is" + self.role + "'s turn"
    def show(self):
        row = {0 : "   ", 1 : " - "}#行
        col = {0 : " ", 1 : "|"}#列
        win = {1 : " 1 ", 0 : " 0 ", -1: " -1"}
        print("   ",end = "")
        for i in range(7):
            print(int(i+1),end = "")
            print("   ",end = "")
        print()
        for i in range(5):
            print(int(i+1),end = "")
            print(": ",end = "")
            for j in range(7):
                print("x", end = "")
                print(row[int(self.board[1][i][j])],end = "")
            print()
            print("   ",end = "")
            if i < 4:
                for j in range(7):
                    print(col[int(self.board[3][i][j])], end = "")
                    if(j < 6):
                        print(win[int(self.showboard[i][j])],end = "")
                print()
        print()

