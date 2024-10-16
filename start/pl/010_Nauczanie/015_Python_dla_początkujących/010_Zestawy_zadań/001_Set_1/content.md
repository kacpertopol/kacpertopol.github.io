<center>
[![](https://upload.wikimedia.org/wikipedia/commons/7/72/Burr%27s_Improved_Nursing_Bottle_1868_Advertisement.jpg)](https://commons.wikimedia.org/wiki/File:Burr%27s_Improved_Nursing_Bottle_1868_Advertisement.jpg)
</center>
<center>
*...functions, numbers, tuples, and lists...*
</center>
<center>
**A**
</center>

<center>
(3 points)
</center>

It's $3$ o'clock in the morning and you need to prepare some formula to feed your newborn baby. The instructions on the package are
very specific: prepare a certain amount of water at a given temperature, add the correct amount of formula, mix 
and cool everything down before serving. In order to keep the baby safe from infections, 
all the water that you use needs to be pre-boiled. Here is your setup:

1. You prepared a container of pre-boiled water
   cooled down to the temperature $T_{\text{cool}}$. 
2. You prepared an empty, sterile feeding bottle.
3. You have an electric kettle and measured that when the water comes out of the spout it has temperature
   $T_{\text{hot}}$ (it's slightly cooler then $100^{\circ}C$).
4. You need to prepare $V$ milliliters (or any other unit of volume) water at temperature $T$ to mix
   up the formula for your little one. You do this by first pouring $V_{\text{cool}}$ milliliters (or any other unit of volume)
   of the cooler water into the bottle and then filling the bottle up to $V$ with the hot water from the kettle. How much cool water 
   should you use?

The mathematics of this problem is very simple, see the **APPENDIX**.
To make things more convenient implement the python function:
```python
def calculateVcool(Tcool , Thot , V , T):
    #...
    return Vcool
```
that returns the volume of the cooler water $V_{\text{cool}}$ you need to pour into the bottle before pouring the remainder
of the water
from the kettle. This volume is calculated in such a way that when mixed the water has temperature $T$. 

Tip: If you find yourself in this scenario a infrared thermometer is a fantastic tool. 

<center>
**B**
</center>

<center>
(1 points)
</center>

Turn the ``V``, ``T``, and ``Thot`` arguments of function ``calculateVcool`` from exercise **A** into 
optional arguments with realistic default values for a $3$
month old baby. 

<center>
**C**
</center>

<center>
(2 points)
</center>

Write a python script that asks the user to input the arguments of ``calculateVcool`` from **A**,
runs the function and prints the result.

<center>
**D**
</center>

<center>
(1 points)
</center>

Nobody has time to fiddle around with their laptop at $3$ o'clock in the morning. Get the script from **C**
to run on your phone (at your own risk :-) ).

<center>
**E**
</center>

<center>
(4 points)
</center>

Your significant other (SO) has the early morning shift with the baby and asked you to prepare a thermos
with pre-boiled water. You have determined the temperature coefficient of the thermos (the mathematics
of this is very simple, see the **APPENDIX**) and need to decide on the temperature of the water 
in the thermos so that in a couple of hours, when your SO needs to prepare the formula, the temperature
of the water in the thermos is appropriate.

To help with this implement the python function:
```python
def calculateTemperature(Tfinal , time , Troom , k , 
        search = (0.0 , 100.0 , 1000)):
    #...
    return T
```    
where ``Tfinal`` is the desired temperature of the water after time ``time``, ``Troom`` is the 
ambient room temperature and ``k`` is the temperature coefficient. The final optional argument 
``search`` determines the parameters
of a numerical simulation that will solve the problem.
The returned value ``T`` is the desired temperature
of water in the thermos.

Use a simple numerical simulation to solve the problem.
In this simulation scan initial water temperature 
candidates in the range ``search[0]`` $\ldots$ 
``search[1]``. The range is divided into ``search[2]`` temperature values. 
For each temperature candidate, the final temperature after time ``time``
is calculated (see **APPENDIX**). Finally, out of all the temperature
candidates, the one whose final temperature is closest to the desired ``Tfinal``
is returned as ``T``. In your implementation please use:

- a list comprehension,
- tuple unpacking,
- the functions \verb|min| and \verb|index|.

Tip: The exponent is available in the ``math`` library. There is no need to install anything, it comes 
built in. Simply use ``from math import exp``

<center>
**APPENDIX**
</center>

When mixing water to arrive at a given temperature, approximately (the notation is the same as in the exercises):
$$
	V_{\text{cool}} = V \frac{T_{\text{hot}} - T}{T_{\text{hot}} - T_{\text{cool}}}
$$
Does it matter if we use $^{\circ}C$ or $^{\circ}K$? Is the formula any different if you prefer to pour the
hot water first?

When water in a container is left in a room with ambient temperature $T_{\text{room}}$ it will gradually, 
over time change it's temperature to match the ambient temperature. This process can be approximately modeled
by the formula:
$$
	\tau(t) = T_{\text{room}} - (T_{\text{room}} - \tau(0)) e^{-t/k}
$$
where $\tau(0)$ is the initial temperature of water in the thermos and $\tau(t)$ is the temperature in the 
thermos after time $t$. The remaining notation is the same as in the exercises. Please note that 
a non-standard definition of the temperature coefficient $k$ is used. The value of this coefficient
can be worked out by measuring the temperature of the water in the thermos at two points in time 
and doing a little algebra.
Does it matter if we use $^{\circ}C$ or $^{\circ}K$? Is the formula any different if you prefer to pour the
hot water first?

<center>
**ADDITONAL MATERIALS**
</center>

- [some miscellaneous notes](---ThisDir---/printable.pdf)
- [simple program in c](---ThisDir---/helloc.c)
- [simple program in python](---ThisDir---/hellopython.py)
  - [... and the module used by this program](---ThisDir---/myhello.py)
- [simple python script](---ThisDir---/myFirstScript.py)
