import random
import matplotlib.pyplot as plt
import burnolie
import epsilon
import effective_e
import ucb
import policy_search
import pylab
import softmax
def learning(algo,arms,horizon):
    x = [0.0] * horizon
    y = [0.0] * horizon
    for i in range(1, horizon - 1):
        l = algo.select_arm()
        algo.update(l, arms[l].pull())
        x[i] = arms[l].p
        for t in algo.value:
            y[i] = y[i] + t

    plt.figure(1)
    plt.plot( x, 'o-')
    plt.title('Learning')
    plt.ylabel('the action choosed')

    plt.figure(2)
    plt.plot(y, 'o-')
    plt.title('Learning')
    plt.ylabel('the sum of expected rewards')

    plt.show()
    return (algo.select_arm(), algo.nt[algo.select_arm()], arms[l].p)

def comparison_of_e(arms,horizon):
    algo1 = epsilon.e_greedy(len(arms), 0.1)
    x1 = [0.0] * horizon
    algo2 = epsilon.e_greedy(len(arms), 0.2)
    x2 = [0.0] * horizon
    algo3 = epsilon.e_greedy(len(arms), 0.3)
    x3 = [0.0] * horizon
    for i in range(1, horizon - 1):
        l1 = algo1.select_arm()
        l2 = algo2.select_arm()
        l3 = algo3.select_arm()
        algo1.update(l1, arms[l1].pull())
        algo2.update(l2, arms[l2].pull())
        algo3.update(l3, arms[l3].pull())
        x1[i] = arms[l1].p
        x2[i] = arms[l2].p
        x3[i] = arms[l3].p
    plt.plot(x1, 'ro')
    plt.plot(x2, 'b+')
    plt.plot(x3, 'kx')
    plt.ylabel("expected payoff")
    plt.xlabel("attempt")
    plt.show()

def regret(algo,arms,horizon):
    x = 0.0
    z = 0.0
    for i in range(0,len(arms) -1):
        if (arms[i].p > z):
            z = arms[i].p
    for i in range(1, horizon):
        l = algo.select_arm()
        algo.update(l, arms[l].pull())
        x = x + z - arms[l].p
    return (x)

def compare_regret(arms,horizon,e):
    e = epsilon.e_greedy(len(arms),e)
    u = ucb.ucb(arms)
    ef = effective_e.e_effective_greedy(len(arms))
    s = softmax.soft_max(len(arms))
    return(regret(e,arms,horizon),regret(u,arms,horizon),regret(ef,arms,horizon),regret(s,arms,horizon))

#the example to try out
#y = [burnolie.bornoli(random.uniform(0,1))]*2
#for i in range(0,2):
#   y[i]=(burnolie.bornoli(random.uniform(0,1)))
#p = policy_search.ps(2,0.1,0)
#s = softmax.soft_max(5)
#e = epsilon.e_greedy(5,0.1)
#u = ucb.ucb(y)
#ef = effective_e.e_effective_greedy(5)
#z = learning(p,y,100000)
#z = compare_regret(y,1000,0.1)
#print(p.track)
#for i in range(0,2):
#   print(y[i].p)
#print(z)