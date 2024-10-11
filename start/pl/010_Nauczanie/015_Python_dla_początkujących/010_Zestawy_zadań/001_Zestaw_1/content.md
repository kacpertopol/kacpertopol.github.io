<center>
**A**
</center>

<center>
(1 punkt)
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
    ...
    return Vcool
```
that returns the volume of the cooler water $V_{\text{cool}}$ you need to pour into the bottle before pouring the remainder
of the water
from the kettle. This volume is calculated in such a way that when mixed the water has temperature $T$. 

Tip: If you find yourself in this scenario a infrared thermometer is a fantastic tool. 


