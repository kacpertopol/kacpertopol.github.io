<center>
**ADDITIONAL METERIALS**
</center>

- [please read this notebook](---ThisDir---/schoedinger.nb)
  - please run *Evaluate Notebook* before reading
  - this is not the end of the story, we will be 
    covering other visualization techniques

<center>
**A**
</center>

<center>
(4 punkt)
</center>

Chose a file with data related to your own work
or something you are currently interested in. 
Implement functions that create `Graphics[...]`
or `Graphics3D[...]` expressions ment to visualize this data.
The point is not to use the built in `Plot`, `ListPlot`,
etc. but create your own implementation from the ground up
... this is a bit of work hence the 4 points :) 

<center>
**B**
</center>

<center>
(2 punkt)
</center>

Using your implmementation from **A**, write 
a *Wolfram Languate* script with a simple 
Command Line Interface (CLI). In a minimal CLI
(you are encouraged to extend this):

- the path of the data files that are to be 
  visualized are passed as positional arguments
- `--help` and `-h` print information to the standard output
  about what the script does and what arguments it can take
- `--verbose` and '-v' produce ... verbose output from the script
  this is usefull for debugging purpouses

Tip: you can use `$ScriptCommandLine` in conjunction with
pattern matching in `Cases` to parse the command line arguments.

<center>
**C**
</center>

<center>
(3 punkt)
</center>

The notebook in the **Additional Materials** contains a
function that soves a certain popular equation in Physics
using `Compile`. Rewrite this function one of the following:

- `c`
- `c++`
- `python` with `numpy` or `pytorch`
- `Fortran`

or some other programming language that compiles to native code. 

Use this implementation with in a program with
a clean, readable CLI.

PS If you like you can also chose some other equation to solve numerically.
Additionally, if you chose to implmement the function from the **Additional Materials**
you can use a simpler integration method - we will be more interested in programming
techniques then precission.
