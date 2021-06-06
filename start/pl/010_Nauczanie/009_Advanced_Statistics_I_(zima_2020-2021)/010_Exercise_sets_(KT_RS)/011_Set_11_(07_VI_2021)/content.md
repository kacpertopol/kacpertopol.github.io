<center>
**A**
</center> 

<center>
(2 points)
</center>

Create sample of size $N=20$ from the normal distribution $N(4,1)$. Now forget that we know the expectation value, so treat data as
coming from $N(x,1)$ distribution. We are interested in estimation of $x$.

a) find sample estimator of the expectation value $E(x)$.
b) find its (usual, frequentists) confidence interval at confidence level $\gamma = 0.9$.
c) assume conjugate prior pdf $p(x)$ as $N(x_0,1)$. Under this assumption find:

   1) posterior pdf $p(x|data,x_0,1)$
   2) posterior expectation value $EV(x)$. Compare with result of *a*.
   3) HDPR for x, at $90\%$ DoB. Compare with result of *b*.

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

      1) find posterior pdf $p(\theta_A,\theta_B | \text{data}, \text{prior parameters} \alpha_A, \beta_A, \alpha_B, \beta_B)$. Make its 2-dim plot.
      2) find posterior pdf for logarithmic odds ratio Lambda : p(Lambda|data, prior parameters $\alpha_A$, $\beta_A$, $\alpha_B$, $\beta_B$). Make its
         plot.
      3) using *b 2* find posterior probability $P(\Lambda>0)$ and $P(\Lambda<0)$ (use normal distribution approximation).
