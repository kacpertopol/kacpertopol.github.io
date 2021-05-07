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
