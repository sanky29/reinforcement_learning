#define the value function
import numpy as np
class policy:
    def __init__(self):
        self.vm = np.array([[1/11]*11 for y in range(441)])

    def return_value(self,i,j,a):
        return(self.vm[i*21 + j][a])

go = policy()
go.vm[441][0] = 1.0
print(go.return_value(1,0,1))