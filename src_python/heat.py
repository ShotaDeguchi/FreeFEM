"""
FDM simulation of steady linear heat equation
solve as Poisson equation
"""

import time
import numpy as np

def poisson_2d(dx, dy, u, b, f, g, n_max = int(1e6), c_tol = 1e-12):
    """
    u: unknown vector
    b: source
    f: Dirichlet boundary condition
    g: Neumann boundary condition
    """
    err = 9999.
    t0 = time.time()
    for n in range(n_max):
        v = u.copy()
        u[1:-1,1:-1] = (dy ** 2 * (v[1:-1,2:] + v[1:-1,:-2]) \
                        + dx ** 2 * (v[2:,1:-1] + v[:-2,1:-1]) \
                        - dx ** 2 * dy ** 2 * b[1:-1,1:-1]) \
                        / (2 * (dx ** 2 + dy ** 2))
        # boundary (f: Dirichlet, g: Neumann)
        u[ 0,:] = f
        u[-1,:] = u[-2,:] + g * dy
        u[:, 0] = u[:, 1] + g * dx
        u[:,-1] = u[:,-2] + g * dx
        # convergence tolerance
        err = np.sqrt(np.sum((u - v) ** 2) / np.sum(v ** 2))
        if n % (n_max / 20) == 0:
            elps = time.time() - t0
            print("n: %d, err: %.6e, elps: %.3f" % (n, err, elps))
            t0 = time.time()
            if err < c_tol:
                print(">>>>> converged, loop terminates now")
                break
    return u

nx, ny = 128, 128
x, y = np.linspace(0., 1., nx), np.linspace(0., 1., ny)
dx, dy = (1. - 0.) / (nx - 1), (1. - 0.) / (ny - 1)
X, Y = np.meshgrid(x, y)

u = np.empty(shape=(nx, ny))   # temperature
b = np.empty(shape=(nx, ny))   # source

b = np.sin(2. * np.pi * (X + Y))
f = 0.    # Dirichlet boundary
g = .05   # Neumann boundary

u = poisson_2d(
    dx, dy, u, b, f, g
)

# save the solution
np.save("./np_array/x_numpy.npy", x)
np.save("./np_array/y_numpy.npy", y)
np.save("./np_array/X_numpy.npy", X)
np.save("./np_array/Y_numpy.npy", Y)
np.save("./np_array/u_numpy.npy", u)
