<center>
**Additional Materials**
</center>

- simple plotting
  - [script](---ThisDir---/set_3.py) with some useful examples
  - [sample image](---ThisDir---/sample_image.png) with some useful examples
  - [line by line](---ThisDir---/set_3.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*


<center>
**A**
</center>

<center>
(2 point)
</center>

Convert the script from the **Additional Materials** into a proper python module

- identify which pieces of code can be bunched together into functions
- add `if(__name__ == "__main__"):...`

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
