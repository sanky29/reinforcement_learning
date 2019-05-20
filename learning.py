import random
import matplotlib.pyplot as plt
import burnolie
import epsilon
import pylab
import time

def learn(arms, e, horizon):
    algo =epsilon.e_greedy(len(arms),e)
    x = [0.0] * horizon
    for i in range(1,horizon-1):
        l = algo.select_arm()
        algo.update(l,arms[l].pull())
        x[i] = arms[l].p
    plt.plot(x,'ro')
    plt.ylabel("expected payoff")
    plt.xlabel("attempt")
    plt.show()
    return(algo.select_arm(), algo.nt[algo.select_arm()], arms[l].p)

n = 5

y = []

for i in range(0,4):
    y.append(burnolie.bornoli(random.uniform(0,1)))

z = learn(y,0.1,10000)

print(z)
for i in range(0,4):
    print(y[i].p)