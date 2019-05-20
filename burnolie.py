import random
class bornoli:
    def __init__(self,p):
        self.p = p

    def pull(self):
        if (random.uniform(0,1) <= self.p):
            return(1)
        else:
            return(0)