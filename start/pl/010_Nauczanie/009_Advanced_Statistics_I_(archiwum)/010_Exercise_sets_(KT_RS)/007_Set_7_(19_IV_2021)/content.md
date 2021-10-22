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
