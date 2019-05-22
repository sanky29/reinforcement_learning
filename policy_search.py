import random

class ps:
    def __init__(self,k,a,b):
        self.value= [0.0]*k
        self.nt = [0.0] * k
        self.a = a
        self.b = b
        self.track = [0.0]*k
        for i in range(0,k ):
            self.track[i] = 1/k

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
        return(min(i,len(self.track) - 1))
    def update(self,i,reward):
        z = self.track[i]
        if (reward == 1):
            for j in range(0,len(self.track)):
                 self.track[j] = self.track[j]*(1 - self.a)
            self.track[i] = z + self.a * (1 - z)
        else:
            for j in range(0, len(self.track)):
                self.track[j] = (self.track[j] + self.b*(1 - self.track[j]))
            self.track[i] = z * (1 - self.b)