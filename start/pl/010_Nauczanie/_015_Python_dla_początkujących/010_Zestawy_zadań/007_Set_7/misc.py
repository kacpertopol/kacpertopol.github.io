# you can expand on this to complete
# exercise E:
class MyNumber:
    addCounter = 0

    def __init__(self, val):
        self.value = val

    def __add__(self, other):
        MyNumber.addCounter += 1
        return MyNumber(self.value + other.value)

    def __repr__(self):
        return repr(self.value)

    def __str__(self):
        return str(self.value)
    
    @classmethod
    def resetCounter(cls):
        cls.addCounter = 0

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ! CAREFUL                              !
# ! THE FOLLOWING CODE IS AN ABOMINATION !
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# you can use it to see how things can
# go terribly wrong ...
class BadHash:
    def __init__(self, val):
        self.value = val
        self.hash = val.__hash__()

    def update(self, newval):
        self.value = newval

    def __hash__(self):
        return self.hash

# NOTE that dictionaries have no __hash__ method but:
# - dictionaries can be turned into tuples
#     {"a" : 123 , "b" : 321}
#   can be turned into
#     (('a' , 123) , ('b' , 123)))
#   and this object has a __hash__ method.
# - tuples can be combined can we can calculate 
#   joint __hash__
#     ((1, 2, 3, "4") , (('a' , 123) , ('b' , 123)))
#   is the previous tuple combined with a tuple of 
#   positional arguments
def veryGeneralFunction(*args, **kwargs):
    print("positional arguments : ", args)
    print("hash of positional arguments : ", args.__hash__())
    print("keyword arguments : ", kwargs)
    print("dictionaries have no __hash__ method! please implement this yourself!")

# decorator for functions that take
# a single argument, using a class:
class FunctionCounter:
    def __init__(self, f):
        self.function = f
        self.counter = 0

    def __call__(self, x):
        self.counter += 1
        return self.function(x)

    def resetCounter(self):
        self.counter = 0

# decorator for functions that take
# a single argument, using a function
# and a global variable:
pygame_game_of_life_template.py
def countCalls(f):
    def inner(x):
        global callsToAnnotatedFunction
        callsToAnnotatedFunction += 1
        return f(x)
    return inner
