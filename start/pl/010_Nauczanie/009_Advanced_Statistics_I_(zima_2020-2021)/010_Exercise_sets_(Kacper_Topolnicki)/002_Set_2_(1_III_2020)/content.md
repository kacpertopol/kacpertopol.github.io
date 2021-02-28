<center>
**Additional Materials**
</center>

- simple plotting
  - [script](---ThisDir---/set_2.py) with some usefull examples
  - [line by line](---ThisDir---/set_2.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*


<center>
**A**
</center>

<center>
(1 point)
</center>

Draw a histogram of random variates generated from $N(3 , 2)$. Compare this histogram with the
PDF for the normal distribution (on the same plot).

<center>
**B**
</center>

<center>
(4 points)
</center>

If we have a function $f(x , y , \ldots)$ of two or more independent random variables $x , y , \ldots$ then it is common
to express the variance of this function as:

$$
\sigma_{t} \approx \sqrt{\left(\frac{\partial f}{\partial x}\right)^{2} \sigma_{x}^{2} + \left(\frac{\partial f}{\partial y}\right)^{2} \sigma_{y}^{2} + \ldots}
$$

Please verify this formula by drawing sets of values of $x , y , \ldots$ from normal distributions, calculating the
resulting values of $f(x , y , \ldots)$ and using `numpy.mean`, `numpy.std`. Please chose a number of different
functions $f$ and investivate the limits of the approximation.

<center>
**C**
</center>

<center>
(2 points)
</center>

Calculate the quantile $x_{p}$ of a $N(0 , 1)$ distributed random variable $X$ for $p = 0.4, 0.6$.
Please compare the result with the appropriate [table](http://users.uj.edu.pl/~ufkamys/BK/kwantyle.pdf).

<center>
**D**
</center>

<center>
(2 points)
</center>

Calculate a histogram of values for the function $2 x + y -3z$
where $x , y , z$ are values of $N(0 , 1) , N(1 , 2) , N(2 , 3)$ distributed, independent, random variables.
Calculate the PDF and compare it to the histogram.

<center>
**E**
</center>

<center>
(2 points)
</center>

Calculate a histogram of values for the function $2 x + y -3z$
where $x , y , z$ are values of $N(0 , 1) , N(1 , 2) , N(2 , 3)$ distributed, independent, random variables.
Calculate the PDF and compare it to the histogram.

<center>
**F**
</center>

<center>
(2 points)
</center>

Draw a histogram of random variables from the [Cauchy](https://docs.scipy.org/doc/scipy/reference/tutorial/stats/continuous.html)
distribution. Compare it to the PDF. The PDF, $f(x)$, for the Cauchy distribution has the following form:

$$
f(x) = \frac{1}{\pi (1 + x^{2})}
$$

<center>
**G**
</center>

<center>
(2 points)
</center>

Calculate the expectation value for the [Cauchy](https://docs.scipy.org/doc/scipy/reference/tutorial/stats/continuous.html)
distribution. 

<center>
**H**
</center>

<center>
(3 points)
</center>

Implement 

```python 
def formatError(number , pm):
	...
```

where `numer` and `pm` are floating point numbers related to the value and error of a random variable
and the return type of the function is a character string with the appropriately formatted value.
