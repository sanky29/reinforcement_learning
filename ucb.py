
import math
#define class for ucb1
import burnolie
class ucb:

    #define constructor
    def __init__(self,arms):

        k = len(arms)
        # define one tracking one as
        self.track = [0.0] * k

        #initate the reward one
        self.q = [0]*k
        for a in range(0,len(arms) -1):
            self.q[a] = arms[a].p
            self.track[a] = self.q[a]
        #define the number of trials
        self.repeatation = [0]*k

    #define method to select arm
    def select_arm(self):

        #select one with maximum value of track
        return(self.track.index(max(self.track)))

    #define update method
    #it takes number of trials and arm
    def update(self,i,n,reward):

        #just update the trak ans repeatation also update reward
        self.repeatation[i] =self.repeatation[i] + 1
        self.q[i] = self.q[i] + ((reward - self.q[i])/self.repeatation[i])
        self.track[i] = self.q[i] + math.sqrt(2*math.log(n))/math.pow(self.repeatation[i],2)