<center>
[![](https://upload.wikimedia.org/wikipedia/commons/4/45/BB-ASCII-art-screenshot-zebra.png)](https://commons.wikimedia.org/wiki/File:BB-ASCII-art-screenshot-zebra.png)
</center>
<center>
*...to is or not to is, dictionaries, loops, flow control, modules and objects...*
</center>

<center>
**A**
</center>

<center>
(2 points)
</center>

Implement a function that takes an arbitrary number of arguments,
say floating point numbers,
and returns a dictionary containing:

- a list containing all the arguments
- the mean of the arguments
- the standard deviation of the arguments

Use this function in a script.

<center>
**B**
</center>

<center>
(3 points)
</center>

Implement a simple [text based game](https://en.wikipedia.org/wiki/Text-based_game). The gameplay
and objective is completely up to you. 

Please base your implementation on the following function:
```python
def updateGameState(state)
    # ...
```
that updates the dictionary `state` in every iteration of the
main game loop:
```python
while(!state["finished"]):
    # ...    
```

At each iteration of the game loop print
the available moves / options available to the player and use the `input`
function to decide on how to proceed with the game play. Use `if`, `else`, and `elif`
statements to decide how the game `state` will evolve. When the game is finished, change
the value of `"finished"` in `state` to `True`. This will cause the main loop of the
game to terminate.

<center>
**C**
</center>

<center>
(3 points)
</center>

Add some elegant [ASCI art](https://en.wikipedia.org/wiki/ASCII_art) to your game.
To do this please import the `sys` module and use the `sys.stdout.write` method
to implement the function:
```python
def showGameState(state):
    # ...
```
that will print a beautiful graphical representation of the game state to "standard output".
Add this function to the main game loop.
Please assume that we are working in a terminal that is $80$ characters wide and $40$ characters tall.

Tips:

- use two nested `for` loops to sweep over all the $80 \times 40$ "pixel" display we use in the game
- use `if` and / or a dictionary to decide what character to put in each "pixel"
- the new line character is `\n`
- this does not have to be very complicated, drawing a map with the location of the player is great but 
  printing some basic information about the game statistics is 
  also fine

<center>
**D**
</center>

<center>
(2 points)
</center>

Implement a "smart" function:
```python
def smartFunction(a , b):
    # ...
    return c
```
that returns the result `c = a + b`. Since this
operation is very laborious and time consuming, the function memorizes previous arguments
`a`, `b` that were passed to it, it also memorizes the result. This is all in the hope that when 
we pass those arguments to the function again it won't have to do all that work, it'll 
just recall the result.

In order to achieve this introduce a global variable `smartFunctionMemory` that will contain a dictionary.
The keys in this dictionary are related to the arguments `a`, `b`, and the values are related to the
results `c`.

What types of arguments can we pass into `smartFunction`?

<center>
**E**
</center>

<center>
(2 points)
</center>

Implement the function:
```python
def readState(path)
    # ...
    return state
```
that reads the state from a file located at path `path`. The contents of this file
is processed to obtain the saved state of a previous game. 

Implement the function:
```python
def writeState(state , path)
    # ...
```
that writes the game state to a file located at path `path`.

Add `readState` before the start of the game loop and `writeState` after the loop to allow the user
to save the game progress.

Tip: Don't worry we'll discuss the details during class :-)

