<center>
**Additional Materials**
</center>

- Mathematica [notebook](---ThisDir---/hdpr.nb) and [pdf](---ThisDir---/hdpr.pdf).

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

