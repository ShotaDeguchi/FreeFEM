"""
visualize simulated data
"""

import numpy as np
import matplotlib.pyplot as plt
import pyevtk

# load the solution as v
x = np.load("./np_array/x_numpy.npy")
y = np.load("./np_array/y_numpy.npy")
X = np.load("./np_array/X_numpy.npy")
Y = np.load("./np_array/Y_numpy.npy")
u = np.load("./np_array/u_numpy.npy")

# visualize as plt
plt.figure(figsize=(6, 5))
plt.scatter(X, Y, c=u, cmap="coolwarm", marker=".", vmin=0., vmax=.1)
plt.colorbar()
plt.xlim(0., 1.)
plt.ylim(0., 1.)
plt.savefig("./output/u_numpy.png")

# visualize as vtk (vtr format)
X = X[:,:,np.newaxis]   # add z-dimension
Y = Y[:,:,np.newaxis]
Z = np.zeros_like(X)
U = u[:,:,np.newaxis]
pyevtk.hl.gridToVTK("./output/u_numpy", 
                    X, Y, Z, 
                    cellData  = {"u": U}, 
                    pointData = {"u": U})


