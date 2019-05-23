import random

class ps:
    def __init__(self,k,a,b):
        self.a = a
        self.b = b
        self.pro = [0.0]*k
        for i in range(0,k ):
            self.pro[i] = 1/k

    def select_arm(self):
        l = random.uniform(0,1)
        i = 0
        j = 0.0
        k = True
        while(k and i < len(self.pro)):
            if (l < self.pro[i] + j):
                k = False
            else:
                j = j + self.pro[i]
                i += 1
        return(min(i,len(self.pro) - 1))
    def update(self,i,reward):
        z = self.pro[i]
        if (reward == 1):
            for j in range(0,len(self.pro)):
                 self.pro[j] = self.pro[j]*(1 - self.a)
            self.pro[i] = z + self.a * (1 - z)
        else:
            for j in range(0, len(self.pro)):
                self.pro[j] = (self.pro[j] + self.b*(1 - self.pro[j]))
            self.pro[i] = z * (1 - self.b)