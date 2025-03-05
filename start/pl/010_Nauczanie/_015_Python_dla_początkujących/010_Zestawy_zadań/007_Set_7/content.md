<center>
[![](https://upload.wikimedia.org/wikipedia/commons/c/cc/Digital_rain_animation_medium_letters_shine.gif)](https://commons.wikimedia.org/wiki/File:Digital_rain_animation_medium_letters_shine.gif)
</center>

<center>
*...magic methods, class functions and the matrix...*
</center>

<center>
**A**
</center>

<center>
(2 points)
</center>

Implement the smart function from exercise **D** in **Set 2**. Use a function decorator.
This decorator is a class with a `__call__` method. Objects of this class also 
have a field that contains a dictionary with previous arguments and return values.

<center>
**B**
</center>

<center>
(2 points)
</center>

Expand the decorator from the previous exercise to accept a function with an 
arbitrary number of arguments positional argument.

<center>
**C**
</center>

<center>
(1 points)
</center>

Expand the decorator from the previous exercise to accept a function that has an arbitrary 
number of positional and keyword arguments.

<center>
**D**
</center>

<center>
(2 points)
</center>

Define a class `BadHash` of mutable integer objects. Each time a new instance
of the object is created, increment a class variable. Add with a `__hash__` method to 
... CAREFULL THIS IS A BIG MISTAKE! But we will go with it to explore the consequences.
Use this method with functions that use our decorator. 

<center>
**E**
</center>

<center>
(4 points)
</center>

Define a class whose objects hold a numerical value. At minimum, the class should
have the following methods apart from the constructor:

- `__add__`, `__sub__` "magic" method to add and subtract objects of this class using the `+` and `-` operators
- `__mul__`, `__truediv__` "magic" methods to multiply and divide objects of this class using the `*` and `/` operators 
- `__neg__` to get the negative number using the `-` operator
- `__str__`, `__repr__` to return the string representation of the number in objects of this class

In addition to performing numerical operations `__add__`, `__sub__`, `__mul__`, `__truediv__`, and `__neg__`
should appropriately increase the four class counters that determine how many additions, multiplications, divisions and 
negations were executed.
Add the following class methods:

- `resetCounters` resets counters that count the number of multiplications, additions, divisions and negations
- `getCounters` returns a tuple with the counters of multiplications, additions, divisions and negations

Use this class to determine the computational complexity of matrix multiplication and calculating 
the application of a matrix to a vector.

<center>
**ADDITIONAL MATERIALS**
</center>

- some [miscellaneous code](---ThisDir---/misc.py) from class, please have a look at the comments
