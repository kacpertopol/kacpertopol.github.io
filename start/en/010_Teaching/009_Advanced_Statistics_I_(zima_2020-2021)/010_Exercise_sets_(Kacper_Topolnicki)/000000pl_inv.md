---
title : Exercise sets
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Zawartość:

* [Set 1 (25 I 2020)](#set-1-25-i-2020)



# Set 1 (25 I 2020)

<center>
**Additional Materials**
</center>

- simple plotting
  - [script](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/plots.py) with simple plots
  - [line by line](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/plots.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- numerical integration
  - [script](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/integrals.py)
  - [line by line](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/integrals.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- `csv` import and export
  - [script](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/numpycsv.py)
  - [line by line](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/numpycsv.pdf) guide to the script (I suggest that you read this first)
    - some comments in the guide do not apply to *Windows*
- additional links
  - [official python 3 tutorial](https://docs.python.org/3/tutorial/)
  - [SciPy website](https://www.scipy.org/)
  - [pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)
  - [plot legends in pyplot](https://matplotlib.org/3.3.3/api/_as_gen/matplotlib.pyplot.legend.html)
  - [scipy quad function for integrals](https://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html)
  - [ipython documentation](https://ipython.readthedocs.io/en/stable/index.html)
 

<center>
**SET 1**
</center>

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

Download the [basic script](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/basic_example.py).
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

Download the [more complicated example](./start/pl/010_Nauczanie/009_Advanced_Statistics_I_(zima_2020-2021)/010_Exercise_sets_(Kacper_Topolnicki)/001_Set_1_(25_I_2020)/more_complex_example.zip).
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

