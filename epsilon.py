#import random library
import random
import numpy
#define class to solve the question
class e_greedy:

    #write intiate funtion
    def __init__(self,k,e):
        #the number of arms
        self.n = k
        #the e value
        self.e = e
        #define number of trails
        self.nt = [0]*k
        #define the expected value till now as
        self.value = [0.0]*k

    def select_arm(my_object):
        #genrate random float
        if (random.uniform(0,1) > my_object.e):
            #now go for exploitation
            return my_object.value.index(max(my_object.value))
        #else do exploration
        else:
            return(random.randint(0,my_object.n -1))

    def update(self, u, reward):
        self.nt[u] += 1
        self.value[u] = self.value[u] + (reward - self.value[u])/(self.nt[u])

o = e_greedy(10,0.999999)
o.update(9,8)
o.update(o.select_arm(),9)
print(o.value)