# FreeFEM
FreeFEM & Python (NumPy) code to solve steady heat equation:
$$ \nabla^2 u (x, y) = \sin(2 \pi (x + y)) $$
with boundary conditions being:
$$ u (x, 0) = 0 $$
$$ \frac{\partial u}{\partial n}(x, 1) = 0.05 $$
$$ \frac{\partial u}{\partial n}(0, y) = \frac{\partial u}{\partial n}(1, y) = 0.05 $$

FreeFEM solves with P1 elements, while NumPy FDM takes regular orthogonal grid, both divide x- & y- domain into 128 subdumains. 

## Solution
|FreeFEM|FDM (NumPy)|
|:---:|:---:|
|<img src="./figures/FreeFEM.png">|<img src="./figures/numpy_FDM.png">|


