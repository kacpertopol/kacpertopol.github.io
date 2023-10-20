---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Content:

* [Set 1](#set-1)
* [Set 2](#set-2)
* [Set 3](#set-3)



# Set 1

<center>
**ADDITIONAL METERIALS**
</center>

- [Hanoi Tower puzzle](https://en.wikipedia.org/wiki/Tower_of_Hanoi)
- [Mandelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set)
- [chaotic notebook from 10 X 2023](./start/en/010_Teaching/012_Numerical_calculatins_in_Mathematica/010_Exercises/001_Set_1/numerical_10-10-2023.nb)
  - CAREFULL: the sceleton for the function solving the hanoi tower is wrong! 
    (Hint: First move the top n-1 from A to B, then move largest disk from A to C and finally move n-1 from B to C.)

<center>
**A**
</center>

<center>
(1 punkt)
</center>

Please install and run the *Mathematica* programm.

<center>
**B**
</center>

<center>
(1 punkty)
</center>

Using the *notebook* interface, please implement the Fibonacci
number sequence.
$0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21, \ldots$.

<center>
**C**
</center>

<center>
(1 punkty)
</center>

Please write a *Wolfram-Language* script that takes one argument
from the command line and returns the corresponding number
from the sequence of Fibonacci numbers
$0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21, \ldots$.

<center>
**D**
</center>

<center>
(2 punkty)
</center>

Suggest a pattern to represent a single configuration of a Hanoi tower.
This pattern can be used to define a type. Implement a function
that uses this pattern and draws the configuration.

<center>
**E**
</center>

<center>
(2 punkty)
</center>

Please write a function that solves the Hanoi tower problem.
In your solution use Curried versions of functions and try
to use only pure functions (no side effects).

<center>
**F**
</center>

<center>
(2 punkty)
</center>

Write a function that calculates the Mandelbrot set (approximation).
Try to make your solution as simple as possible and use only functions
and methods that are not unique to Mathematica.




# Set 2

<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](./start/en/010_Teaching/012_Numerical_calculatins_in_Mathematica/010_Exercises/002_Set_2/hanoi.nb)
  - detailed information about the Hanoi Tower puzzle
- exercises **A**-**C** are marked as additional exercises
  - points from these exercises will not be used when determing 
    the grading curve
  - nontheless I encourage you to try and solve them

<center>
**A (additional challenge)**
</center>

<center>
(3 punkt)
</center>

Mathematica is an very flexible language and can be used to prototype
different styles of programming. Introduction of types can lead to 
a style that mimics object oriented programming. 
More interesting, at least in my opinion, is the possibility to 
program in a functional style.

We have seen how to 
implement the *hsif* (inverse *fish*) operator for the
Hanoi tower in order to keep track of the history without
having to resort to dirty tricks such as side effects.

Please implement new *bind* and *hsif* functions such that, for example if:
```
possibilitiesAfter[x_] := {x + 1 , x - 1};
otherPossibilitiesAfter[x] := {x + I , x - I};
```
then
```
(otherPossibilitiesAfter ~ hsif	~ possibilitiesAfter)[1]
```
results in (some ordering of):
```
{2 + I , 2 - I , 1 + I , 1 - I}
```

In other words this new *bind* and *hsif* allows us to compose functions that 
return alternative possibilities (for example of things happening).

<center>
**B (additional challenge)**
</center>

<center>
(2 punkt)
</center>

A nice feature of the functional approach is that we can use equational reasoning 
about our programm. Please check if the [monad laws](https://wiki.haskell.org/Monad_laws)
are satisfied in **A**. 

Tip: `>==` is `bind`.

<center>
**C (additional challenge)**
</center>

<center>
(3 punkt)
</center>

Similar to **A** but this time *bind* and *hsif* allow us to compose
functions that can return an error. 

Tip: have a look at [the maybe monad](https://wiki.haskell.org/Maybe).

<center>
**D**
</center>

<center>
(2 punkt)
</center>

Create an animation of the solution to the Hanoi tower. 
First try to implement a function that draws a
single state of the puzzle. Next try `Manipulate` or `ListAnimate`.

Try to export this solution as a `GIF`.

Tip: Use the built in language for graphics. 


# Set 3

<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](./start/en/010_Teaching/012_Numerical_calculatins_in_Mathematica/010_Exercises/003_Set_3/julia_fractal.nb)
  - please run *Evaluate Notebook* before reading
  - [Julia set](https://mathworld.wolfram.com/JuliaSet.html)

<center>
**D**
</center>

<center>
(2 punkt)
</center>

Turn your implementation of the Mandelbrot set from the **Set 1**
into a compiled function. Using `AbsoluteTiming` compare the speed
of the implementation with different `CompilationTarget` and `Parallelization`.

<center>
**E**
</center>

<center>
(2 punkt)
</center>

Implement the calculation of the Mandelbrot set using
a more traditional compiled language, `C` or `FORTRAN`.
Try to use the same algorithm. Compare the speed
to the compiled functions in `Mathematica`.



