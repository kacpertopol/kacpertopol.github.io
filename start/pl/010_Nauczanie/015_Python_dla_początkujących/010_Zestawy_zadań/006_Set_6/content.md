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
[the game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
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
(4 points)
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
**ADDITIONAL MATERIALS**
</center>

- [some code from class 28-11-2025](---ThisDir---/argparse_example.py)

... Obtaining the number of neighbours for the basic 
[game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) ...

Let's assume that we start from random configuration of $4 \times 4$ cells:

```python
import numpy as np                                        # 1
s = 4                                                     # 2
state = np.random.randint(0 , high = 2 , size = (s , s))  # 3
print(state)                                              # 4
```

In **1** we import the `numpy` library, in **2** we set the size of the matrix
containing cell states, in **3** we draw a random distribution of cells (0 meaning a dead cell
1 meaning a live cell, the integers
are drawn from a uniform distribution between $0$ and `high - 1` $= 1$). Finally **4**
prints our result:

```
[[0 0 0 0]
 [0 1 1 0]
 [1 1 0 1]
 [0 1 0 1]]
```
To get a table whose values at a specific row and column correspond the state if the eight
neighbors (Up, Down , Right , Left , UpRight , DownLeft , UpLeft, DownRight) we first `roll`
the arrays to obtain:

```python
U = np.roll(state , 1 , axis = 0)
D = np.roll(state , -1 , axis = 0)
R = np.roll(state , -1 , axis = 1)
L = np.roll(state , 1 , axis = 1)
UR = np.roll(np.roll(state , 1 , axis = 0) , -1 , axis = 1)
DL = np.roll(np.roll(state , -1 , axis = 0) , 1 , axis = 1)
UL = np.roll(np.roll(state , 1 , axis = 0) , 1 , axis = 1)
DR = np.roll(np.roll(state , -1 , axis = 0) , -1 , axis = 1)
```
and then sum:

```python
neighbors = U + D + R + L + UR + DL + UL + DR
print(neighbors)
```
as a result, each cell has the following number of neighbors:
```
[[3 3 4 2]
 [4 3 3 3]
 [5 4 6 3]
 [5 2 4 2]]
 ```
 This should be correct if we assume periodic boundaries
 (the left edge is glued to the right edge and the top edge is glued to the
 bottom edge).

 The next bit is tricky. There are many ways of implementing a single iteration of the game.
 Since we are looking to eliminate regular python loops to increase the speed of our program
 have a look at the following functions `np.ones`, `np.zeros`, `np.where`, `np.logical_and`,
 `np.logical_or` and then have a close look the following code:

 ```python
 allAlive = np.ones((s , s) , dtype = np.int64)
 allDead = np.zeros((s , s) , dtype = np.int64)
 np.where(np.logical_and(state == 0 , neighbors == 3) , allAlive , state)
 ```

This can be easily extended to include the whole set of rules of the game. 
Remember stick to `numpy` for performance.

... The same thing but this time with convolutions ...

Let's import the `convolve2d` function from the `scipy.signal` library.
Note that we are not importing the whole package nut just one function:

```python
from scipy.signal import convolve2d
```

Next let's try this:

```python
k = np.array([[1 , 1 , 1] , [1 , 0 , 1] , [1 , 1 , 1]])
neighborsWithConvolve2D = convolve2d(state , k , mode = "same" , boundary="wrap")
print(neighborsWithConvolve2D)
```

The result should be the same as `neighbors`:

```
[[3 3 4 2]
 [4 3 3 3]
 [5 4 6 3]
 [5 2 4 2]]
```

The result is the same but the method is more general.
We can look at a wider neighborhood of a cell by
modifying `k`.

... The user input is all wrong ...

Tip: Saving a `numpy` array can be obtained by running `np.save` (or `numpy.save` if we used just `import numpy`).
Loading a `numpy` array can be obtained by running `np.load`. Both these functions raise exceptions if they get a
bad file path. This means that we can use them inside `try:` and `except:` blocks. The function `int` also
raised exceptions when it's string argument is not a correctly formatted integer.

... Hiding class members ...

A nice article on name mangling at [geeksforgeeks](https://www.geeksforgeeks.org/name-mangling-in-python/).

... Calculating the hash of a numpy array ...

To calculate the hash of the data that is contained inside a `numpy` array `a` try `hash(a.data.tobytes())`.

... Implementation using [pygame](https://www.pygame.org/docs/) ...

See the [pygame](https://www.pygame.org/docs/) website for installation instructions. 
To implement the game of life, both the classic version and the smooth version, you can
use the [template](---ThisDir---/pygame_game_of_life_template.py). Please read the comments
from the template carefully.

