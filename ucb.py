
import math
#define class for ucb1
import burnolie
class ucb:

    #define constructor
    def __init__(self,arms):
        self.n = 0
        k = len(arms)
        # define one tracking one as
        self.track = [0.0] * k

        #initate the reward one
        self.value = [0]*k
        for a in range(0,len(arms) -1):
            self.value[a] = arms[a].p
            self.track[a] = self.value[a]
        #define the number of trials
        self.nt = [0]*k

    #define method to select arm
    def select_arm(self):

        #select one with maximum value of track
        return(self.track.index(max(self.track)))

    #define update method
    #it takes number of trials and arm
    def update(self,i,reward):
        self.n =+ 1
        #just update the trak ans repeatation also update reward
        self.nt[i] =self.nt[i] + 1
        self.value[i] = self.value[i] + ((reward - self.value[i])/self.nt[i])
        self.track[i] = self.value[i] + math.sqrt(2*math.log(self.n))/math.pow(self.nt[i],2)