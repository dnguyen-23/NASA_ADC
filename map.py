import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator
import scipy
dim = 1277
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

x = np.arange(0, dim, 1)
# print(x.shape)
y = np.arange(0, dim, 1)
# print(y.shape)

# x = np.genfromtxt('FY20 ADC Regional Data File LONGITUDE.csv', delimiter=',', dtype=None)
# y = np.genfromtxt('FY20 ADC Regional Data File LATITUDE.csv', delimiter=',', dtype=None)
z = np.genfromtxt('FY20 ADC Regional Data File HEIGHT.csv', delimiter=',', dtype=None) / 100
z = z[:dim, :dim] #z needs to have dims of the mesh

X, Y = np.meshgrid(x, y)
# surf = ax.plot_surface(x, y, z, cmap=cm.terrain, linewidth = 0, antialiased = False)
# Z = scipy.interpolate.griddata((xs, ys), zs, X, Y)


ax.set_zlim(-1.01, 1.01)
surf = ax.plot_surface(X, Y, z, rstride=5, cstride=5, cmap=cm.jet,
                       linewidth=1, antialiased=True)


fig.colorbar(surf)
ax.set_zlim(-100, 100)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter('{x:.02f}')

fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()