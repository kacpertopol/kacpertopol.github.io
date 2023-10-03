#!/usr/bin/env python3

# klasa implementująca liczby dualne
#
# Dual(a , b) <-> a + b * epsilon

class Dual:
    def __init__(self , one , epsilon):
        self.one = one
        self.epsilon = epsilon

    def __add__(self , other):
        if(isinstance(other , Dual)):
            newone = self.one + other.one
            newepsilon = self.epsilon + other.epsilon
            return Dual(newone , newepsilon)
        else:
            return Dual(self.one + other , self.epsilon)

    __radd__ = __add__

    def __sub__(self , other):
        if(isinstance(other , Dual)):
            newone = self.one - other.one
            newepsilon = self.epsilon - other.epsilon
            return Dual(newone , newepsilon)
        else:
            return Dual(self.one - other , self.epsilon)

    __rsub__ = __sub__

    def __mul__(self , other):
        if(isinstance(other , Dual)):
            newone = self.one * other.one
            newepsilon = self.one * other.epsilon + self.epsilon * other.one
            return Dual(newone , newepsilon)
        else:
            return Dual(self.one * other , self.epsilon * other)

    __rmul__ = __mul__

    def __neg__(self):
        return Dual(-self.one , -self.epsilon)

    def __str__(self):
        return str(self.one) + " + epsilon * " + str(self.epsilon)
    
    def __repr__(self):
        return str(self.one) + " + epsilon * " + str(self.epsilon)

# definicja funkcji exp, którą można wykorzystać z liczbami dualnymi
# 
# n - obcięcie szeregu
# x - argument exp(x)

def expSeries(n , x):
    value = 1.0
    numerator = 1.0
    denominator = 1.0
    for k in range(1 , n):
        numerator *= x
        denominator *= k
        value += numerator * (1.0 / denominator)
    return value

# definicja funkcji sin, którą można wykorzystać z liczbami dualnymi
# 
# n - obcięcie szeregu
# x - argument sin(x)

def sinSeries(n , x):
    numerator = x
    denominator = 1.0
    sign = 1.0
    value = x
    for k in range(1 , n):
        numerator *= x * x
        denominator *= (2 * k + 1) * (2 * k)
        sign *= -1.0
        value += sign * numerator * (1.0 / denominator)
    return value

# definicja funkcji cos, którą można wykorzystać z liczbami dualnymi
# 
# n - obcięcie szeregu
# x - argument cos(x)

def cosSeries(n , x):
    numerator = 1.0
    denominator = 1.0
    sign = 1.0
    value = 1.0
    for k in range(1 , n):
        numerator *= x * x
        denominator *= (2 * k) * (2 * k - 1)
        sign *= -1.0
        value += sign * numerator * (1.0 / denominator)
    return value

if(__name__ == "__main__"):
    print("")
    print("Sprawdzamy proste przykłady ...")
    x = Dual(1.0 , 1.0)
    y = Dual(1.0 , 1.0)
    print("x + y = " , x + y)
    print("x * y = " , x * y)
    print("x * 2 = " , x * 2)
    print("2 * x = " , 2 * x)
    print("x + 2 = " , x + 2)
    print("2 + x = " , 2 + x)
    print("")
    print("Sprawdzamy czy exp'(x) = exp(x) ...")
    x = Dual(1.0 , 1.0)
    print("x = " , x)
    print("expSeries(10 , x) = " , expSeries(10 , x))
    print("")
    print("Sprawdzamy czy sin'(x) = cos(x) oraz cos'(x) = -sin(x) ...")
    x = Dual(2.0 , 1.0)
    print("x = " , x)
    print("sinSeries(10 , x) = " , sinSeries(10 , x))
    print("cosSeries(10 , x) = " , cosSeries(10 , x))
