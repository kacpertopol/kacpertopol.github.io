<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](---ThisDir---/hanoi.nb)
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
