<center>
**ADDITIONAL METERIALS**
</center>

- [scarry](---ThisDir---/kern.nb)
  - please read the notebook
  - some changes
    - fixed en error in the three dimensional laplacian kernel, we need to divide by $hhh^{2}$ and not $hhh^{3}$ 
	- changed the plot from `Image3D` to `ListContourPlot3D` - looks prettier
  - **WARNING** 
    - please **DO NOT** run *Evaluate Notebook* before reading
	- I'm getting a strange Mathematica bug when running this notebook
	- there might be some memory leaks or buffer overflows in to the x window system / graphics card
	- mathematica is working so hard on calculating the eigenvalues that the screen goes black ...
	- **RUN AT YOUR OWN RISK**

<center>
**A**
</center>

<center>
(2 punkt)
</center>

To fix the scary problems outlined in the **ADDITONAL MATERIALS**, delegate the large eigen value problem to *numpy* or some external tool.

<center>
**B**
</center>

<center>
(3 punkt)
</center>

Take apart the final implementation of the function that creates the matrix representation.
Figure how the function works.
Apply it to a different differential equation.

<center>
**C**
</center>

<center>
(4 punkt)
</center>

Read *tutorial/ModularityAndTheNamingOfThings#5934*. Implement 
a package that solves the wave equation for given initial conditions.
Use your immagination - implement the functionality that you yourself
would expect from such a package.

<center>
**D**
</center>

<center>
(2 punkt)
</center>

Investivate why *Compile* does not make the function from the notebook in the
**Additional Materials** faster.
