<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Jan_%C5%81ukasiewicz.jpg/320px-Jan_%C5%81ukasiewicz.jpg)](https://en.wikipedia.org/wiki/Jan_%C5%81ukasiewicz#/media/File:Jan_%C5%81ukasiewicz.jpg)
</center>
<center>
*...modules, packages, first look at classes and objects, ...*
</center>

<center>
**A**
</center>

<center>
(3 points)
</center>

Implement a [Reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation) calculator. 
Base your program on a stack implemented as a python `list`. All operations of the calculator 
take the stack, modify it and return the modified stack. For example adding two numbers:

```python
def add(stack):
    x = stack.pop()      # 1
    y = stack.pop()      # 2
    stack.append(x + y)  # 3
    return stack         # 4
```

At **1** a number is popped from the end of the list with `pop` resulting in a shorter stack. 
At **2** another number is popped from the stack. Finally in **3** the stack is modified by adding
a number to the end of the list with `append`. The new stack, shorter by one number, is returned in **4**.

Add more functions:

- multiply two numbers
- print the stack (does not modify the stack)
- print the last value from the stack 
- using the `math` module add several more mathematical operations
- print some help information (does not modify the stack)
- "quit" adds `None` to the stack

Refer to the functions from a dictionary whose keys are python strings - the names of the functions.
The values in the dictionaries are the functions themselves.

Create a `while` loop that checks if `None` is in the stack using `in`, if it's in the stack - exit.
In the loop ask the user to enter the command name, run the appropriate command from the dictionary
to modify the stack. If the command is not in the dictionary keys, assume that the user entered
a floating point number and append it to the stack.

<center>
**B**
</center>

<center>
(1 points)
</center>

Make the code from **A** a little more bullet proof:

- make sure that the functions from **A** check if there are enough elements on the stack
- make sure that when the user enters a number to push to the stack - it is a properly formatted floating
  point number (tip: use `try` and `except`, we will discuss this during class)

<center>
**C**
</center>

<center>
(2 points)
</center>

Add another module `extra.py` with additional functions. Modify **A** to look inside this module
for additional functions (tip: use the `__dict__` attribute, we will discuss this during class).

<center>
**D**
</center>

<center>
(2 points)
</center>

Implement a simple class that iterates over the [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_sequence).
The constructor takes one argument - the number of Fibonacci numbers to iterate over. We will discuss
the details during class.

<center>
**ADDITONAL MATERIALS**
</center>

- [some miscellaneous materials from class](---ThisDir---/python_for_beginners_08-11-2024.zip)
