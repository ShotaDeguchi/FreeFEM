# FreeFEM
FreeFEM & Python (NumPy) code to solve steady heat equation. 

## Code
### src_FreeFEM
Install FreeFEM from [here](https://freefem.org/), and execute codes in <code>./src_FreeFEM/</code>. They include meshing arbitrary shape into FEM elements (e.g. <code>01_square.d</code>), and heat diffusion simulation.

### src_python
Dependencies for Python code are listed in <code>./src_python/requirements.txt</code>. 

## Solution
The following are simulation results of heat equation whose form is:
$$ \nabla^2 u (x, y) = \sin(2 \pi (x + y)) $$
with boundary conditions being:
$$ u (x, 0) = 0 $$
$$ \frac{\partial u}{\partial n}(x, 1) = 0.05 $$
$$ \frac{\partial u}{\partial n}(0, y) = \frac{\partial u}{\partial n}(1, y) = 0.05 $$

FreeFEM solves with P1 elements, while NumPy FDM takes regular orthogonal grid, both divide x- & y- domain into 128 subdomains. 

|FreeFEM|FDM (NumPy)|
|:---:|:---:|
|<img src="./figures/FreeFEM.png">|<img src="./figures/numpy_FDM.png">|


