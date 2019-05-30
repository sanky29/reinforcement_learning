import policy
import value
import probability
import poisson
import spicy.linalg as slin
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def end_v(g,p,r):
	return(np.dot((np.linalg.inv(np.identity(441) - g*p)),r))

def refine_p(p,e,v):
    for i in range(0,441):
        ans = np.array([[0.0]*11 for x in range(441)])
        x = np.array([0.0]*11)
        y = np.array([0.0]*11)
        for j in range(0,441):
            for z in range(0,11):
                x[z] = x[z] +  e[i][j][z]/441
                y[z] = y[z] + p[i][j][z]*v[i*21 + j]
            indices = np.where((y+0.9*x) == (y+0.9*x).max())
            for l in range(0,len(indices[0])):
                ans[i*21+j][indices[0][l]] = 1/len(indices[0])
        return(ans)

def policy_irit(go,poli,g):
    value = end_v(g,go.return_simple_matrix(poli),go.return_expected_matrix(poli))
    pin = refine_p(go.pm,go.rm,value)
    poli.vm = pin
    for i in range(100):
        value = end_v(g,go.return_simple_matrix(poli),go.return_expected_matrix(poli))
        pin = refine_p(go.pm,go.rm,value)
        poli.vm = pin
    a = [[0.0]*21]*21
    for i in range(0,21):
        for j in range(0,21):
            a[i][j] = value[i*21+j]
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    X = [0]*441
    for i in range(0,441):
        X[i] = i%21
    Y = [0] * 441
    for i in range(0, 441):
        Y[i] = i // 21
    Z = [0] * 441
    for i in range(0, 441):
        Z[i] = value[Y[i]*21+X[i]]
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');
    ax.scatter(X, Y, Z, c='r', marker='o')
    plt.show()




