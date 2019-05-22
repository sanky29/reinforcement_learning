#import random library
import random
import numpy
import math

#define class to solve the question
class e_effective_greedy:

    #write intiate funtion
    def __init__(self,k,):
        #the number of arms
        self.n = k
        #define number of trails
        self.nt = [0]*k
        #define the expected value till now as
        self.value = [0.0]*k
        self.time = 1

    def select_arm(my_object):
        #genrate random float
        if (random.uniform(0,1) > 1/((math.log(my_object.time)) + 1)):
            #now go for exploitation
            return my_object.value.index(max(my_object.value))
        #else do exploration
        else:
            return(random.randint(0,my_object.n -1))

    def update(self, u, reward):
        self.time = self.time + 1
        self.nt[u] += 1
        self.value[u] = self.value[u] + (reward - self.value[u])/(self.nt[u])

