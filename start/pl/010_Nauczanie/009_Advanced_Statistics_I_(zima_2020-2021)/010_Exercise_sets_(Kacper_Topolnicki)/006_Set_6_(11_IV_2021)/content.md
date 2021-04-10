<center>
**Additional Materials**
</center>

- sample script with statistical tests for checking if
  data is sampled from a normal distribution
  - [script](---ThisDir---/set_5.py) with some useful examples
  - [line by line](---ThisDir---/set_5.pdf) guide to the script (I suggest that you read this first)
- a convenient way of adding a command line interface is by using the [argparse](https://docs.python.org/3/library/argparse.html)
  library
  - as a side effect this can help you document your code

<center>
**A**
</center>

<center>
(2 point)
</center>

Please visit the [datahub](https://datahub.io/)
website. Change the sample script to test
a few chosen datasets.

<center>
**B**
</center>

<center>
(3 points)
</center>

Modify the script:

- add a command line interface
- given a path to a CSV file or the URL of a 
  CSV file the script should produce a probability plot
- optional arguments change the distribution 

<center>
**C**
</center>

<center>
(3 points)
</center> 

Modify the script:

- add a command line interface
- given a path to a CSV file or the URL of a 
  CSV file the script should run the ShapiroWilk test

<center>
**D**
</center>

<center>
(3 points)
</center> 

Create your own version of a function that creates a probablility plot
for a given distribution. You can use the various distributions
defined in th `scipy.stats` library 
(see the [documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)).
Most of these distributions have methods that implement the precent point function
(`ppf`) and and that allow you to draw random numbers from these distributions (`rvs`).
As the quantile levels you can use: $\frac{1}{N+1}, \frac{2}{N+1}, \ldots, \frac{N}{N+1}$
where $N$ is the sample size.

The input to your function should be:

- a list with data
- a distrubution

The result of execution the function should include
a probability plot with a least-squares linear fit using `scipy.stats.linregress` 
([documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)). 
Additionally the r-value should be returned.

<center>
**E**
</center>

<center>
(2 points)
</center> 

Using **D** compare probability plots and r-values between your implementation and `stats.probplot`.
Use data sampled directly from $N(0 , 1)$ and sample sizes equal to $6 , 15 , 50 , 200$. 
Discuss the difference between the r-values.

<center>
**F**
</center>

<center>
(2 points)
</center> 

Using `stats.probplot`, investigate the probobility plots for the following distributions:

- uniform distribution in the range $(-0.8 , 0.8)$
- uniform distribution in the range $(-3 , 3)$
- uniform distribution in the range $(-15 , 15)$
- t student's distribution with 3 degrees of freedom
- t student's distribution with 20 degrees of freedom
- Weibull distribution with $a = 8.9$ (shape parameter), $b = 1.5$ (scale parameter)
- Weibull distribution with $a = 1.5$ (shape parameter), $b = 5$ (scale parameter)
- a combination of two normal distributions $N(-a , b)$, $N(k_{1} a , k_{2} b)$ 
  (the sample sizes should be around $30$ for each normal distribution and, initially, $a = 2$, $b = 1$, $k_{1} = k_{2} = 1$)

Use different sample sizes as in **E**. 


Tip: see the [documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)

