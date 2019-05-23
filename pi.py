import random
class gradient:

    def __init__(self,arms):
        assert (len(arms) == 2)
        self.pro = [0.5]*2
        self.t = 0.5

    def select_arm(self):
        l = random.uniform(0,1)
        if (l > self.pro[0]):
            return(1)
        else:
            return(0)

    def update(self,i,reward):
        self.t = self.t + 0.3*reward*(i - self.t)
        self.pro[0] = 1 - self.t
        self.pro[1] = self.t

