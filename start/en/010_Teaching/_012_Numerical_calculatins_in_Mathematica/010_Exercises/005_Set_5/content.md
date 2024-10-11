<center>
**ADDITIONAL METERIALS**
</center>

- [notebook and c code](---ThisDir---/simplesch.zip)
  - please read the notebook
    - please DON't run *Evaluate Notebook* before reading
    - evaluate cells as you read

<center>
**A**
</center>

<center>
(2 punkt)
</center>

Write a function in Mathematica that runs the shell command `date`
parses the standard output from this command and returns the time and date.

<center>
**B**
</center>

<center>
(3 punkt)
</center>

Change the implementation in `sch.c` (alternatively you can use some other programm)
to write the result to standard output (is this better, faster?). Change the notebook from the **Additional Materials**
to read and parse the result from standard output.

<center>
**C**
</center>

<center>
(4 punkt)
</center>

The notebook from the **Additional Materials** runs a single process with `sch`. Please
modify the code to run `sch` in parallel for different specifications of the potential. 
Wrap everything up in a single function.

Tip: Have a look at `StartProcess`. 
