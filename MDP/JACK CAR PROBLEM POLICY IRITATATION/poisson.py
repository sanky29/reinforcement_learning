#define function for probability calculation
import numpy as np
import math
class poisson:

    def __init__(self,lembda,n):
        self.l = lembda
        self.pro = np.array([0.0]*(n+1))
        self.total = 0.0
        for i in range(0,n+1):
            self.pro[i] = math.exp(-1*self.l)*math.pow(self.l,i)/math.factorial(i)
            self.total += self.pro[i]

    def get_pro(self,n):
        return(self.pro[n])


