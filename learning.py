import random
import matplotlib.pyplot as plt
import burnolie
import epsilon
import effective_e
import ucb
import pylab
import time

def learn_simple(arms, e, horizon):
    algo =epsilon.e_greedy(len(arms),e)
    x = [0.0] * horizon
    y = [0.0] * horizon

    for i in range(1,horizon-1):
        l = algo.select_arm()
        algo.update(l,arms[l].pull())
        x[i] = arms[l].p
        for t in algo.value:
            y[i] = y[i] + t
    plt.plot(y,'r-')
    plt.ylabel("expected payoff")
    plt.xlabel("attempt")
    plt.show()
    return(algo.select_arm(), algo.nt[algo.select_arm()], arms[l].p)

def learn_effective(arms, horizon):
    algo =effective_e.e_effective_greedy(len(arms))
    x = [0.0] * horizon
    y = [0]*horizon
    for i in range(1,horizon-1):
        l = algo.select_arm()
        algo.update(l,arms[l].pull())
        x[i] = arms[l].p
        for t in algo.value:
            y[i] = y[i] + t
    plt.plot(y,'r-')
    plt.ylabel("expected payoff")
    plt.xlabel("attempt")
    plt.show()
    return(algo.select_arm(), algo.nt[algo.select_arm()], arms[l].p)

def learn_more_effective(arms, horizon):
    algo =ucb.ucb(arms)
    x = [0.0] * horizon
    y = [0.0]*horizon
    for i in range(1,horizon):
        l = algo.select_arm()
        algo.update(l,i,arms[l].pull())
        x[i] = arms[l].p
        for t in algo.q:
            y[i] = y[i] + t
    plt.plot(y,'r-')
    plt.ylabel("expected payoff")
    plt.xlabel("attempt")
    plt.show()
    return(algo.select_arm(), algo.repeatation[algo.select_arm()],algo.q[algo.select_arm()], arms[l].p)

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

def regret_ucb(arms,horizon):
    algo = ucb.ucb(arms)
    x = 0.0
    z = 0.0
    for i in range(0,len(arms) -1):
        if (arms[i].p > z):
            z = arms[i].p
    for i in range(1, horizon):
        l = algo.select_arm()
        algo.update(l, i, arms[l].pull())
        x = x + z - arms[l].p
    return (x)
def regret_egreedy(arms,horizon,e):
    algo = epsilon.e_greedy(len(arms),e)
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

def regret_effect(arms,horizon):
    algo = effective_e.e_effective_greedy(len(arms))
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
    return(regret_egreedy(arms,horizon,e),regret_effect(arms,horizon),  regret_ucb(arms,horizon))