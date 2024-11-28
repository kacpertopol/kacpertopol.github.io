<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](---ThisDir---/wstp_example.nb)
  - please don't run `Evaluate Notebook`
  - evaluate the cells one by one 
  - [simple c program](---ThisDir---/julia_set.c)
  - [simple template file](---ThisDir---/julia_set.tm)

<center>
**A**
</center>

<center>
(2 punkt)
</center>

Please write a C language function (similar to `julia_set.c`) that can be used
to calculate the Mandelbrot set. Use WSTP to call this function from Mathematica.

<center>
**B**
</center>

<center>
(3 punkt)
</center>

Write two C language functions (in the same file).
Make sure that they are set up in to be called from Mathematica using WSTP.

The first function `setA(int a)` sets the value of a global variable to a.
Ths second function `returnA()` returns the value of the global variable.

Compile and test these functions in Mathemaica. 
Is the global variable state persistant after we call `Install` from Mathematica?

Hint: You can add multiple functions to the template file. 
Each function starts with `:Begin:` and ends with `:End:`. For functions that don't return a result 
try `WSPutSymbol(stdlink , "Null")`.

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Collect the code from **A** and **B**. Use a Makefile to compile the code.
