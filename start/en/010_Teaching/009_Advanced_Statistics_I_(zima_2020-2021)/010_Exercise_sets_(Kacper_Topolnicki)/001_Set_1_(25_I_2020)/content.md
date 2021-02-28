<center>
**Additional Materials**
</center>

- simple plotting
  - [script](---ThisDir---/plots.py) with simple plots
  - [line by line](---ThisDir---/plots.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- numerical integration
  - [script](---ThisDir---/integrals.py)
  - [line by line](---ThisDir---/integrals.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- `csv` import and export
  - [script](---ThisDir---/numpycsv.py)
  - [line by line](---ThisDir---/numpycsv.pdf) guide to the script (I suggest that you read this first)
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

Download the [basic script](---ThisDir---/basic_example.py).
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

Download the [more complicated example](---ThisDir---/more_complex_example.zip).
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
