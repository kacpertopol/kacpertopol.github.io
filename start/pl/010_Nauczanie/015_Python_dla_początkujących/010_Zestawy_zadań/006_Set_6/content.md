<center>
[![](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)](https://en.wikipedia.org/wiki/File:Gospers_glider_gun.gif)
</center>

<center>
*...life, numpy, matplotlib, more on classes and exceptions...*
</center>

<center>
**A**
</center>

<center>
(2 points)
</center>

Using the `numpy` library please implement 
[the game of life](https://upload.wikimedia.org/wikipedia/commons/e/e5/Gospers_glider_gun.gif)
with periodic boundary conditions (the left half of the grid is glued to the right, the 
top part of the grid is glued to the bottom ... essentially creating a torus).
The implementation should be a single script.
The grid of cells is represented by a `numpy` array with an integer `dtype`. 
When implementing a single iteration of the game, please stick to the `numpy` library
as strictly as possible to boost performance. Test the performance using large
grids (1920 by 1080 and larger). 

Tip: Use the `numpy.roll` function to obtain the state of neighbouring cells. Visualization
can be achieved using the `matplotlib.pyplot` library functions,
[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) or
[`matshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html) function.
We will cover the basic usage of `matplotlib` during class.

<center>
**B**
</center>

<center>
(2 points)
</center>

Extend **A** to continuous values: the state of the cell can be dead (0), alive (1)
or anything in between. There are many sensible ways of doing this. One way is "smooth life", see
the links:

- [online simulation](https://smooth-life.netlify.app/)
- [pre-print](http://arxiv.org/abs/1111.1567)

Tip: The function 
[`convolve2d`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve2d.html) 
from the `scipy` might be helpful. It works with `numpy` arrays.
Visualization
can be achieved using the `matplotlib.pyplot` library functions,
[`imshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html) or
[`matshow`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.matshow.html) function.
We will cover the basic usage of `matplotlib` during class.

<center>
**C**
</center>

<center>
(2 points)
</center>

Add a simple interactive command line interface to **A** or **B**. The program should
give the user at least the following options:

- save state of the game (the grid of cells) into a file with specified path
- load state of the game (the grid of cells) from a file with specified path
- run a specified amount of iterations
- quit

Be persistent, if the user types an incorrect value prompt him / her again. To do this use `try`,
`except`.

<center>
**D**
</center>

<center>
(2 points)
</center>

Wrap everything (**A** + **C** or **B** + **C**) into a class. Place the class
definition in a separate module and use this module in a script. 

<center>
**E**
</center>

<center>
(2 points)
</center>

Write a wrapper for the `numpy` array representing a grid of cells in the game of life.
Try to make this class immutable (is this really possible in python?). 
Add the `__hash__` and `__eq__` methods to the class.

<center>
**F**
</center>

<center>
(2 points)
</center>

Implement the smart function from exercise **D** in set 2. Use a function decorator.
This decorator is a class with a `__call__` method. 
