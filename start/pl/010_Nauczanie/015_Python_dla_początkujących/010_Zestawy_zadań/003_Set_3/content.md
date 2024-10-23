<center>
[![](https://upload.wikimedia.org/wikipedia/en/6/62/Literate_Programming_book_cover.jpg)](https://en.wikipedia.org/wiki/Literate_programming)
</center>
<center>
*...literate programming, loops and lambdas, ...*
</center>

<center>
**A**
</center>

<center>
(2 points)
</center>

Replace the repeated `if`, `elif`, `else` statements from your game in **Set 2** with `match`.
If these statements don't appear in the game, please add some.

<center>
**B**
</center>

<center>
(2 points)
</center>

End your scripts from **Set 1** with an infinite `while` loop instead of a call similar to `input("Hit enter to exit.")`.
Please use `pass` in the infinite loop. 

Import the `time` module and use the `time.time()` function to measure the time the program spends in the loop.
If this time exceeds $10$ seconds, ask the user if the program should exit. If the program is supposed to wait
reset the timer and run the loop for another $10$ seconds.

Tip: use `continue`, and `break`.

<center>
**C**
</center>

<center>
(4 points)
</center>

Using the [Jupyter notebook](https://jupyter.org/) please investigate the [logistic map](https://en.wikipedia.org/wiki/Logistic_map).

Create a function that calculates the logistic map and draw the map using the `matplotlib` library, we will discuss how this library works during class. 
Make sure the notebook
has a detailed description of your approach, use [literate programming](https://en.wikipedia.org/wiki/Literate_programming).

<center>
**C**
</center>

<center>
(2 points)
</center>

Re-implement the function from **C** to accept a keyword argument `drawFunction`. If the value of this keyword
argument is not the default `None` then `drawFunction` points to a function that draws the data and a plot of the 
logistic map is produced automatically.

Test if this works using a `lambda` expression.

Can you use `is` to check if `drawFunction` has the default value?
