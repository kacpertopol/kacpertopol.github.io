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

