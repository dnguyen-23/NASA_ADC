import numpy as np
from mpl_toolkits import mplot3d
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv

numVert = 1277**2
x = np.genfromtxt('NASA_ADC_latitude.csv', delimiter=',', dtype=None)
y = np.genfromtxt('NASA_ADC_longitude.csv', delimiter=',', dtype=None)
z = np.genfromtxt('NASA_ADC_height.csv', delimiter=',', dtype=None)
print(x.shape)
print(y.shape)
print(z.shape)
# print(np.max(x), "  ", (np.max(x) - x[0][0]))
# print(np.min(y), "   ", np.max(y), "  ", (y[0][0]))
# print("First row min: ", min(x[0]), "first row max: ", max(x[0]))
# print("init", x[0][0], " last: ", x[0][len(x[0]) - 1])
# print("first row min: ", min(y[0]), "first row max: ", max(y[0]))
# print("init", y[0][0], " last: ", y[0][len(y[0]) - 1])

def testGraph():
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    
    ax.scatter3D()


def graph():
    X = (x.flatten()[0: numVert] - x[0][0]) * 100 / np.max(x)
    Y = (y.flatten()[0: numVert] - y[0][0]) * 100 / np.max(y)
    Z = z.flatten()[0: numVert] / 1000

    # X, Y = np.meshgrid(x, y)

    print(X.shape)
    print(Y.shape)
    print(Z.shape)
    fig = plt.figure()


    ax = plt.axes(projection='3d')
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
    ax.scatter3D(X, Y, Z, c=Z, cmap='Greens')
    ax.set_title('surface')

    plt.show()