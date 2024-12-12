<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Palmer_Method_sample.jpg/1024px-Palmer_Method_sample.jpg)](https://commons.wikimedia.org/wiki/File:Palmer_Method_sample.jpg)
</center>

<center>
*...pretty strings...*
</center>

<center>
**A**
</center>

<center>
(1 + 1 points)
</center>

In an era before electronic calculators, logarithms were king. 
Two usefull properties of the logarithm function:
$$
\log{a b} = \log{a} + \log{b}
$$
$$
\log{a / b} = \log{a} - \log{b}
$$
make it possible to change multiplication and division into 
addition and subtraction which require much less effort.
This observation lies at the heart two interesting old calculating methods:
[the slide rule](https://en.wikipedia.org/wiki/Slide_rule), and
[tables of logarithms](https://en.wikipedia.org/wiki/Mathematical_table#Tables_of_logarithms).
We will be focusing on the latter.

Please read [this section](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
on fancier string formatting and create a string containing table of logarithms: 

```
-------------------
| x     |  Log(x) |
-------------------
| 1.00  |  0.0000 |
| 1.01  |  0.0043 |
| 1.02  |  0.0086 |
...
| 1.20  |  0.0792 |
...
| 2.00  |  0.3010 |
...
| 6.00  |  0.7782 |
...
| 10.0  |  1.0000 |
-------------------

```
the first column has numbers going from $1$ to $10$ (the step size is up to you). The second columns 
is a base $10$ logarithm of the corresponding number in the first column.

How can we use this table in practice. Let's say we want to multiply $2$ by $6$:
$$
\log_{10}{2 \times 6} = \log_{10}{2} + \log_{10}{6} \approx 0.3010 + 0.7782 = 1.0792 = \log_{10}{x}
$$
where $x$ is our approximate result ($\approx 12$). 
We can approximate the logarithms by looking at our table and addition is easy enough
(a person equipped with only a book of logarithm tables and an abacus is a dangerous
calculating machine).
There is a problem though, if we look at the second column the value $1.0792$ is out of range, how do we solve this?
Simple, just subtract $1$ (or divide by $10$ depending on how you look at it):
$$
\log_{10}(x / 10) = \log_{10}{x} - \log_{10}{10} = 1.0792 - 1.0 = 0.0792
$$
The value $0.0792$ is no longer out of range in the second column and corresponds to ... $1.20$ which is 
our apporximate (we are doing approximations here left and right, let's not forget about this)
result divided by $10$. So to summarize logarithm tables, plus some extra tricks like dividing by ten 
or subtracting one, are a powerful calculating tool.

Save your table into a text file. Make sure that:

- the columns have consistent width
  - one option is to round the numbers to a set precision
  - other options are available [in the tutorial](https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting)
- the table has a header 
- the extra points is for using [block elements](https://en.wikipedia.org/wiki/Block_Elements) instead 
  of `|` and `+` in drawing the frame of the table

Hint: logarithms are available in the `math` library. To calculate the base $10$ logarithm of $2.0$ 
you can use `math.log(2.0 , 10)`.

<center>
**B**
</center>

<center>
(3 points)
</center>

Change the formatting of your logarithm table to use 
[$\LaTeX$ syntax for tables](https://www.overleaf.com/learn/latex/Tables).
Make the table larger and split it into multiple separate tables.
Each page should contain a single table.
Add special values for $\pi$, $\e$ etc.
Can we add more columns to perform calculations with square roots and trigonometric functions?

Save the string with your table into a file with a `.tex` extension. Compile it with $\LaTeX$.

