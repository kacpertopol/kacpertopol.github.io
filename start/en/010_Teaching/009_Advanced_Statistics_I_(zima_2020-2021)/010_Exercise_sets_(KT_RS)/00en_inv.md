---
title : Exercise sets
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Content:

* [Set 1 (25 I 2021)](#set-1-25-i-2021)
* [Set 2 (1 III 2021)](#set-2-1-iii-2021)
* [Set 3 (8 III 2021)](#set-3-8-iii-2021)
* [Set 4 (15 III 2021)](#set-4-15-iii-2021)
* [Set 5 (22 III 2021)](#set-5-22-iii-2021)
* [Set 6 (11 IV 2021)](#set-6-11-iv-2021)
* [Set 7 (19 IV 2021)](#set-7-19-iv-2021)
* [Set 8 (10 V 2021)](#set-8-10-v-2021)
* [Set 9 (24 V 2021)](#set-9-24-v-2021)
* [Set 10 (31 V 2021)](#set-10-31-v-2021)
* [Set 11 (07 VI 2021)](#set-11-07-vi-2021)



# Set 1 (25 I 2021)

<center>
**Additional Materials**
</center>

- simple plotting
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/plots.py) with simple plots
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/plots.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- numerical integration
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/integrals.py)
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/integrals.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- `csv` import and export
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/numpycsv.py)
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/numpycsv.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- additional links
  - [official python 3 tutorial](https://docs.python.org/3/tutorial/)
  - [SciPy website](https://www.scipy.org/)
  - [pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)
  - [plot legends in pyplot](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.legend.html)
  - [scipy quad function for integrals](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html)
  - [ipython documentation](https://ipython.readthedocs.io/en/stable/index.html)
 

<center>
**A**
</center>

<center>
(1 point)
</center>

Follow the instructions on the [*SciPy* webpage](https://www.scipy.org/)
and install the *SciPy* python ecosystem.

<center>
**B**
</center>

<center>
(1 point)
</center>

Download the [basic script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/basic_example.py).
Run this script using one of the two following methods:

- navigate to the script directory in the terminal (command line) and run `python basic_example.py`
- (this method will probably not work on Windows) navigate to the script directory, permit the script to be executed using `chmod +x basic_example.py` and run `./basic_example.py`

You can also try and use `ipython` to execute commands from this script one by one.

<center>
**C**
</center>

<center>
(3 points)
</center>

Download the [more complicated example](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/001_Set_1_(25_I_2021)/more_complex_example.zip).
Unpack this directory, carefully read the *README.pdf* file and try running the *compress.py*
script.

This example does not have much to do with statistics but it demonstrates the 
powerful capabilities of the `numpy` library. Please rewrite this script without
using `numpy` and compare execution times of both implementations.

<center>
**D**
</center>

<center>
(2 points)
</center>

Plot the function $f(x) = \left(\sin{x^{2}}\right)^{2}$ for $0 < x < \sqrt{2 \pi}$ and calculate the integral
$\int_{0}^{\sqrt{2 \pi}} f(x) dx$ using *SciPy*.


# Set 2 (1 III 2021)

<center>
**Additional Materials**
</center>

- simple plotting
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/002_Set_2_(1_III_2021)/set_2.py) with some usefull examples
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/002_Set_2_(1_III_2021)/set_2.pdf) guide to the script (I suggest that you read this first)
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


# Set 3 (8 III 2021)

<center>
**Additional Materials**
</center>

- simpe de-noising, background removal
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/003_Set_3_(8_III_2021)/set_3.py) with some useful examples
  - [sample image](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/003_Set_3_(8_III_2021)/sample_image.png) with some useful examples
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/003_Set_3_(8_III_2021)/set_3.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
  - [module template](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/003_Set_3_(8_III_2021)/module_template.py)


<center>
**A**
</center>

<center>
(2 point)
</center>

Convert the script from the **Additional Materials** into a proper python module

- identify which pieces of code can be bunched together into functions
- add `if(__name__ == "__main__"):...`

[tip](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/003_Set_3_(8_III_2021)/module_template.py)

<center>
**B**
</center>

<center>
(2 points)
</center>

Construct a 5 by 5 `float64` matrix (two dimensional array, an array with two axis) in numpy:

- the diagonal elements are $-1$
- the elements just above and just below the diagonal are $\frac{1}{2}$
- the last element in the first row is $\frac{1}{2}$
- the last element in the first column is $\frac{1}{2}$
- all other elements are $0$

[tip](https://numpy.org/doc/stable/reference/generated/numpy.diag.html)

<center>
**C**
</center>

<center>
(4 points)
</center>

Construct a matrix with elements as in **B** but the size is 100 by 100.
Calculate it's eigenvalues and eigenvectors using 
[`numpy.linalg.eig`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html).
Draw the eigenvectors using `matplotlib`. What does the matrix represent?


# Set 4 (15 III 2021)

*IMPORTANT: This set is ment for students familiar with python.
Points from these exercises will not be taken into account when
estimating the grading curve. They will only be added to your point total
only if you obtained enough points from the other sets.*

<center>
**Additional Materials**
</center>

- regular expressions
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/004_Set_4_(15_III_2021)/set_4.py) with a simple example
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/004_Set_4_(15_III_2021)/set_4.pdf) guide to the script

<center>
**A**
</center>

<center>
(3 point)
</center>

Have a look at the [script from the previous set](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/004_Set_4_(15_III_2021)/../003_Set_3_(8_III_2021)/set_3.py)
and try to improve it:

- Separating the text from the background (signal from the noise) assumes that the pixel
  values are normally distributed around some mean value. Is this a good assumption?
  Can you make a better one, and improve the de-noising procedure? How / why does the improvement
  increase the quality of the resulting image?
- Add a command line interface.

<center>
**B**
</center>

<center>
(2 points)
</center>

Assemble a collection of your articles or articles by your favorite collaborators.
Extract the raw text from those papers. You can try the following methods

- use the LaTeX source
- use [pdftotext](https://pypi.org/project/pdftotext/)

<center>
**C**
</center>

<center>
(3 points)
</center>

Extract floating point numbers from the texts of the articles in **B**. Use this data
to test [Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law) 


# Set 5 (22 III 2021)

*IMPORTANT: This set is ment for students familiar with python.
Points from these exercises will not be taken into account when
estimating the grading curve. They will only be added to your point total
only if you obtained enough points from the other sets.*

<center>
**A**
</center>

<center>
(2 point)
</center>

Using the publication texts from the previous set:

- compile a list of distinct characters in these texts (this includes the various
  types of whitespaces) and calculate the frequency with which these characters appear in the text 
- truncate the text so that it's length would be a multiple of 2 and compile a list of distinct character
  pairs, calculate their frequency in the text
- truncate the text so that it's length would be a multiple of 3 and compile a list of distinct character
  triplets, calculate their frequency in the text

<center>
**B**
</center>

<center>
(2 points)
</center>

Compile the same type of data as in **A** but this time using python code for the text. 
You can use the sample scripts from the previous sets, but since they contain a lot
of natural language it would be better to grab code from [online repositories](https://github.com/search?l=&o=desc&q=language%3APython&s=stars&type=Repositories).

<center>
**C**
</center>

<center>
(3 points)
</center> 

Use the results of **A** and **B** to calculate the [Shanon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
of these texts

$$H(X) = - \sum_{i = 1}^{N} P(x_{i}) log_{2}(P(x_{i}))$$

where $X$ is a random variable whose $N$ possible values $x_{i}$ are distributed with probability $P(x_{i})$ and

- $x_{i}$ are distinct single characters
- $x_{i}$ are distinct character pairs
- $x_{i}$ are distinct character triplets

Discuss the result.


# Set 6 (11 IV 2021)

<center>
**Additional Materials**
</center>

- sample script with statistical tests for checking if
  data is sampled from a normal distribution
  - [script](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/006_Set_6_(11_IV_2021)/set_5.py) with some useful examples
  - [line by line](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/006_Set_6_(11_IV_2021)/set_5.pdf) guide to the script (I suggest that you read this first)
- a convenient way of adding a command line interface is by using the [argparse](https://docs.python.org/3/library/argparse.html)
  library
  - as a side effect this can help you document your code
- tip vrom V.U:
  - you can skip the creation of the temporary file by using the `pandas.read_csv` metod directly applied to a URL

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
where $N$ is the sample size. As theoretical quantiles these for N(0,1) or N(a,b) should be used, where a and b are sample estimators
of expectation value and variance, respectively.

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
Use data sampled directly from $N(0 , 1)$ and sample sizes equal to $6 , 15 , 30, 50 , 200$. 
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
- t-Student distribution with 3 degrees of freedom
- t-Student distribution with 20 degrees of freedom
- Weibull distribution with $a = 8.9$ (shape parameter), $b = 1.5$ (scale parameter)
- Weibull distribution with $a = 1.5$ (shape parameter), $b = 5$ (scale parameter)
- a combination of two normal distributions $N(-a , b)$, $N(k_{1} a , k_{2} b)$ 
  (the sample sizes should be around $30$ for each normal distribution and, initially, $a = 2$, $b = 1$, $k_{1} = k_{2} = 1$)

Use different sample sizes as in **E**. 


Tip: see the [documentation](https://docs.scipy.org/doc/scipy/reference/stats.html)



# Set 7 (19 IV 2021)

<center>
**ADDITIONAL MATERIALS**
</center>

Interpolation using `scipy`:

- [1D interpolation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d)
  - see the code examples in the link
- [2D interpolation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp2d.html#scipy.interpolate.interp2d) (for future reference)

<center>
**A**
</center>

<center>
(2 point)
</center>

Draw a two-sampled Q-Q plot, i.e. a plot with the horizontal axis related to sample 1, the vertical axis related to sample 2.
The ranges of the axis are the same as the ranges of the samples.
Each point is given by empirical quantiles, i.e. (X,Y)=(empirical quantile of order i of sample 1, empirical quantile of order i of sample 2).
If the size of the samples is the same, plot the order of empirical quantiles i(find it as for Normal P-plot) is not important (orders will be the same for both samples)
Just plot one sample versus another one.
If sizes of samples are not equal, interpolate quantiles for the bigger sample to orders of quantiles obtained for smaller sample.

Check how it works for:

- two samples of the same size (N=10, N=50) from the same normal distribution
- two samples of the same size (N=10, N=50) from two normal distributions which differs in EV only.
- two samples of the same size (N=10, N=50) from two normal distributions which differs in STD only.
- two samples of the same size (N=10, N=50) from two normal distributions which differs both in EV and STD.
- two samples of the same size (N=10, N=50), one from normal distribution, another from uniform distribution.

<center>
**B**
</center>

<center>
(2 point)
</center>

Draw a two-sampled P-P plot, i.e. plot with horizontal axis related to sample 1, vertical axis related to sample 2.
Ranges of both axes are between 0 and 1.
Each point is given by the empirical CDF calculated as the order of the corresponding quantile (X,Y)=(order of empirical quantile of sample 1,
order of empirical quantile of sample 2)
If sizes of samples are not equal, suitable interpolation is needed.

<center>
**C**
</center>

<center>
(2 point)
</center>

Probability correlation coefficient plot
Draw a sample S of size N=30 from a N(0, 0.25) distribution.
Now, forget that we know the variance of that distribution.
Find it using the probability correlation coefficient plot. To do that:

- Find the correlation coefficients for Normal P-plots between sample S and theoretical distribution of N(0,v)
  on a grid of v in a big range (0-...).
- Next build a probability correlation coefficient plot: 
    - on the horizontal axis put the v parameter, on the vertical - the obtained correlation coefficient.
    - The maximum in this plot will point the estimator of v. Compare it with the true value 0.25. 

<center>
**D**
</center>

<center>
(2 point)
</center>

<center>
(Additional problem, do only if you solved other problems)
</center>

In
<https://en.wikipedia.org/wiki/Tukey_lambda_distribution>
you can find a formula for quantiles Q of the Tukey-lambda distribution. This distribution covers many other distributions depending on the value of
its parameter $\lambda$. It can be used to recognize the type of distribution.
As in Problem 3: Draw a sample S of size N=30 from N(0, 0.25) the distribution.
Now, forget that we know variance of that distribution, and even the type of distribution.

Find correlation coefficients for P-plots between sample S and theoretical Tukey-lambda distribution with parameter lambda
on grid of lambda in range (-1,1).
Next build a probability correlation coefficient plot: on horizontal axis put parameter lambda, on vertical the obtained correlation coefficient.
The value of lambda for which maximum is observed can be interpreted as

- $\lambda$ = −1 approx. Cauchy C(0,π)
- $\lambda$ = 0 exactly logistic
- $\lambda$ = 0.14 approx. normal N(0, 2.142)
- $\lambda$ = 0.5 strictly concave
- $\lambda$ = 1 exactly uniform U(−1, 1)
- $\lambda$ = 2 exactly uniform U(−1/2, 1/2)

See also "comments" section on the same web page.


# Set 8 (10 V 2021)

<center>
**Additional Materials**
</center>

- Runs Test 
  - [link 1](https://online.stat.psu.edu/stat415/book/export/html/837)
  - [link 2](https://empslocal.ex.ac.uk/people/staff/dbs202/cag/courses/MT37C/course/node14.html)
- box plot
  - [matplotlib documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.boxplot.html)

<center>
**A**
</center> 

<center>
(2 points)
</center>

Using the Shapiro-Wilk test (at signifcance level 0.05) check the normality of following N-element samples.
In each case repeat test for few samples - find how often test gives correct result.

- sample drawn from the normal distribution $N(3,9)$ for $N=10$ and $N=50$
- sample drawn from the uniform distribution $[-1.5,1.5]$ for $N=10$ and $N=100$
- sample drawn from the uniform distribution $[-10,10]$ for $N=10$ and $N=100$
- sample drawn from the t-Student distribution with number of degrees of freedom = 1 and 10
- sample drawn from the Chi-2 distribution with number of degrees of freedom = 3

Program the run test using formulas from the lecture.

<center>
**B**
</center>

<center>
(2 points)
</center>

Using run tests check randomness of the following sample:
```
AAABBBAAABBBAAABAAABABABBAABABBABBAAABBBAAABBB
```

<center>
**D**
</center>

<center>
(2 points)
</center>

Using run test check if two samples come from the same distribution. Use samples from:

- one sample $N=15$ from $N(0,1)$, another $N=15$ from $N(x,1)$ for $-5<x<5$ step $0.1$
- one sample $N=15$ from $N(0,1)$, another $N=15$ from $N(0,x)$ for $-4<x<4$ step $0.2$
- one sample $N=15$ from $N(0,1)$, another $N=15$ from uniform distribution $[-2, 2]$
- one sample $N=15$ from $N(0,1)$, another $N=15$ from uniform distribution $[-10, 10]$

In each  case print (after combinining and ordering two probes) sequences and try to guess answer before doing test.

<center>
**E**
</center>

<center>
(2 points)
</center>

Create a boxplot for a given sample and in one figure show
(verticaly, side by side) five boxplots together with the sample elements drawn from:

- $N(0,1)$ with size $N=8$
- $N(0,1)$ with size $N=30$
- Cauchy distribution ($x0=0$, $gamma=3$) with size $N=30$
- same sample as in the first point but supplemented, by hand, with one outlier element far from rest of the sample
- same sample as in the first point but supplemented, by hand, with group of close five outlier elements far from rest of the sample


# Set 9 (24 V 2021)

<center>
**Additional Materials**
</center>

- [GESD](https://towardsdatascience.com/anomaly-detection-with-generalized-extreme-studentized-deviate-in-python-f350075900e2)
- [Hampel](https://towardsdatascience.com/outlier-detection-with-hampel-filter-85ddf523c73d)
- Orthogonal distance regression
	- [example](https://www.tutorialspoint.com/scipy/scipy_odr.htm)
	- [python documentation](https://docs.scipy.org/doc/scipy/reference/odr.html)
- Lest squares fitting
	- [example](https://towardsdatascience.com/least-squares-linear-regression-in-python-54b87fc49e77#:~:text=As%20the%20name%20implies%2C%20the,predicted%20by%20the%20linear%20approximation.)
	- [python documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html)

<center>
**A**
</center> 

<center>
(2 points)
</center>

Basing on formulas from the lecture program the Hampel ([additional link](https://towardsdatascience.com/outlier-detection-with-hampel-filter-85ddf523c73d)) test. Next:

1. Apply it to data sampled from $N(0,1)$ with size $N=10$ supplemented, by hand, with one outlier element far (but not very far) from rest of the sample.
2. Repeat 1 but add one more datum point between the outlier and its neighbor. Check if result of test depends
on position of this new point.

<center>
**B**
</center> 

<center>
(2 points)
</center>

Create a sample $X$ from $N(0,1)$ with size $N=20$ and add four outlier points at the same time: one for
small $X$ (e.g. $x = -5$) and three for big $X$ (e.g. $X = 7.2$, $X = 7.6$ , $X = 20$).
Use the generalized ESD ([GESD](https://towardsdatascience.com/anomaly-detection-with-generalized-extreme-studentized-deviate-in-python-f350075900e2)) test to detect number of outliers (and outliers itself).
Check how results of test depend on position of outliers, for example move point $X = 7.2$ towards main group of points, e.g. to $X = 3.5$ or smaller.

<center>
**C**
</center>

<center>
(2 points)
</center>

Linear regression $Y= a X + b$ including uncertainties of $Y$.

Create a sample of $(X,Y)$ pairs to simulate linear regression:
for $X = 1.0 , 1.2 , 1.4 , ... , 4.8$ (so size is $N=20$) draw $Y$ from $N(2 X - 0.3 , 0.09)$ (so standard deviation of each $Y_i$ is $0.3$).
Thus "real" parameters of regression are $a=2$ and $b=-0.3$.
Now forget that you know these parameters and find their estimators and uncertainties from prepared data using linear weighted regression.

Next add outliers:

1. one outlier point $(10, Y_{0})$ with uncertainty of $Y_{0}$ equals $0.3$. Apply regression again and plot $a$, uncertainty($a$),$b$, and uncertainty($b$)
as a function of $Y_{0}$ in range $(5, 25)$
2. one outlier point $(3.1, Y_{0})$ with uncertainty of $Y_{0}$ equals $0.3$. Apply regression again and plot 1, uncertainty($a$),$b$, and uncertainty($b$)
as a function of $Y_{0}$ in range $(-10, 10)$. Compare plots from subpoints 1 and 2.
3. as in 1 but with uncertainty of $Y_{0}$ equals $0.03$. Compare plots from subpoints 1 and 3.  

<center>
**D**
</center>

<center>
(2 points)
</center>

<center>
*additional exercise*
</center>

Repeat problem **C**, but use linear regression based on minimizing absolute deviations (LAD Method).



# Set 10 (31 V 2021)

<center>
**Additional Materials**
</center>

- Mathematica [notebook](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/010_Set_10_(31_V_2021)/hdpr.nb) and [pdf](./start/en/010_Teaching/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(KT_RS)/010_Set_10_(31_V_2021)/hdpr.pdf).

<center>
**A**
</center> 

<center>
(2 points)
</center>

We will be working with the normal distribution $N(E(X) , var(X))=N(2,4)$. Please execute the following sub-points for two sizes of sample: $N=15$ and $N=50$.
After doing sub-points a - c please compare the obtained results.

a) True characteristics: find (analytically, using Python command) 1st, 2nd (median), and 3rd quartile. Calculate IQR (interquartile range).
b) True characteristics based on sampling: sample $M=50000$ $N$-element samples from $N(2,4)$. For each sample find
estimators of all quartiles and IQR. Basing on $50000$ samples plot their (quartiles and IQR) histograms and find estimators of their standard deviations.
c) Bootstrap estimator: sample one more $N$-element probe from $N(2,4)$. Find resulting estimators for all quartiles and IQR.
Make corresponding boxplot (skip whiskers).
Apply to this specific sample bootstrap resampling creating $B=10000$ bootstrap samples of the same size $N$.
For each bootstrap sample find
estimators of all quartiles and IQR. Basing on $10000$ bootstrap samples plot their (quartiles and IQR) histograms and find bootstrap estimators of their IQRs.  

<center>
**B**
</center> 

<center>
(2 points)
</center>

<center>
*additional exercise* 
</center>

Repeat A. but for Weibull distribution with parameters $\lambda = 1$ and $k=1.5$ - this is example of asymmetric probability density function.

<center>
**C**
</center>

<center>
(2 points)
</center>

Like A but for bivariate normal distribution and correlation coefficient.

We will be working with the bivariate normal distribution with $E(X)=0$, $E(Y)=2$, $SDV(X)=1$, $SDV(Y)=1$, and two values of correlation
coefficient: $CORR(X,Y)=0.9$ and $CORR(X,Y)=0.2$.
Please perform following subpoints for two sizes of sample: $N=15$ and $N=50$ and both $CORR(X,Y)$.
After doing subpoints a - b please compare obtained results.

a) Sample N-element bivariate probe. Make a plot. Calculate point estimator for correlation coefficient.
b) Apply to sample from a bootstrap resampling creating $B=10000$ bootstrap samples of the same size $N$.
For each bootstrap sample find estimator of correlation coefficient. Plot its histogram and find bootstrap estimators of IQR for correlation coefficient.

<center>
**D**
</center>

<center>
(2 points)
</center>

For N(2,1) find the HDPR at 68% degree of belief.

<center>
**E**
</center>

<center>
(2 points)
</center>

For a probability density function $f(x)=0.5 [N(0,1)+N(4,2.25)]$ (where $N(a,b)$ is $N(E(X),var(X))$ so SDV is $1.5$ for
the second distribution) find the HDPR at 90% degree of belief.



# Set 11 (07 VI 2021)

<center>
**A**
</center> 

<center>
(2 points)
</center>

Create sample of size $N=20$ from the normal distribution $N(4,1)$. Now forget that we know the expectation value, so treat data as
coming from $N(x,1)$ distribution. We are interested in estimation of $x$.

a) find sample estimator of the expectation value E(x).
b) find its (usual, frequentists) confidence interval at confidence level gamma=0.9.
c) assume conjugate prior pdf p(x) as N(x_0,1). Under this assumption find:

   1) posterior pdf $p(x|data,x_0,1)$
   2) posterior expectation value $EV(x)$. Compare with result of *a*.
   3) HDPR for x, at $90%$ DoB. Compare with result of b).

d) make sensitivity analysis, i.e. repeat *c* for $x_0$ in $[1,7]$, step $0.2$, make plot showing *c 2* and *c 3* as a function of $x_0$.

<center>
**B**
</center> 

<center>
(2 points)
</center>

a) Using initial sample and results from the previous problem (at given $x_0$) find Bayes factor
for null hypothesis H0: $x \le 3.0$ and alternative hypothesis $x > 3.0$.
b) (additional exercise) make plot showing Bayes factor as a function of prior $x_0$.

<center>
**C**
</center> 

<center>
(2 points)
</center>

Patients' favourable responses to the two drugs were compared. 50 out of 250 respondents responded to drug A, and 40 out of 250
responded to drug B. We would like to compare if one drug is better than another. Both drugs have been tested independently.
a) find sample estimator of the expectation values for efficiency of both drugs (fraction of patient with response) $\theta_A$ and $\theta_B$,
respectively. Compare them.
Are they equal?

b) Assume conjugate bivariate prior pdf for ($\theta_A$, $\theta_B$) in form of the product of two Beta distributions with parameters
($\alpha_A$, $\beta_A$) and ($\alpha_B$, $\beta_B$). Repeat this and following points twice: one assuming uninformative prior, and one assuming any other values
of parameters you like (in range of possible values).
In both cases:  

   1) find posterior pdf $p(\theta_A,\theta_B | \text{data})$, prior parameters $\alpha_A$, $\beta_A$, $\alpha_B$, $\beta_B$). Make its 2-dim plot.
   2) find posterior pdf for logarithmic odds ratio Lambda : p(Lambda|data, prior parameters $\alpha_A$, $\beta_A$, $\alpha_B$, $\beta_B$). Make its
plot.
   3) using *b 2* find posterior probability $P(\Lambda>0)$ and $P(\Lambda<0)$ (use normal distribution approximation).

