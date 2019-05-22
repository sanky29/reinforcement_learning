import random
import math
class soft_max:
    def __init__(self,k):
        self.value = [0.0]*k
        self.nt = [0]*k
        self.track = [0.0]*k
        for i in range(0,k ):
            self.track[i] = i/k
        self.o = k
        print(self.track)
    def select_arm(self):
        l = random.uniform(0,1)
        i = 0
        j = 0.0
        k = True
        while(k and i < len(self.track)):
            if (l < self.track[i] + j):
                k = False
            else:
                j = j + self.track[i]
                i += 1
        return(i)
    def update(self,i,reward):
        self.nt[i] += 1
        p = self.value[i]
        k = len(self.nt)
        self.value[i] = self.value[i] + ((reward - self.value[i])/self.nt[i])
        self.o = self.o + math.exp(self.value[i]) -  math.exp(p)
        for i in range(0,k ):
            self.track[i] = math.exp(self.value[i])/self.o