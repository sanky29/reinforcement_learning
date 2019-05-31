#define the value function
import numpy as np
#define the value function
class value:
    def __init__(self):
        self.vm = np.array([0.0]*441)

    def return_value(self,i,j):
        return(self.vm[i + j*21])


