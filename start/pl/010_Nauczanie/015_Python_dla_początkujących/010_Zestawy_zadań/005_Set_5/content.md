<center>
[![](https://upload.wikimedia.org/wikipedia/commons/b/bd/Enigma_%28crittografia%29_-_Museo_scienza_e_tecnologia_Milano.jpg)](https://commons.wikimedia.org/wiki/File:Enigma_(crittografia)_-_Museo_scienza_e_tecnologia_Milano.jpg)
</center>

<center>
*...dictionaries, ciphers, and more on files...*
</center>

<center>
**A**
</center>

<center>
(2 points + 1 point)
</center>

Implement two functions.
The first one encodes the plaintext ... `plaintext` (string of characters):
```python
def encode(key , plaintext):
    # ...
    # return ciphertext
```
and the second one decodes the ciphertext ... `ciphertext` (string of characters):
```python
def decode(key , ciphertext):
    # ...
    # return plaintext
```
Both functions take a string of characters, `key`, as the first argument.

Use any cipher you like. We will discuss options during class. The extra point is for interesting solutions.

<center>
**B**
</center>

<center>
(2 points)
</center>

Rewrite the functions from **A**.
Implement `encoder` and `decoder` so that they can be used:
```python
myEncoder = encoder("secret_key")
myDecoder = decoder("secret_key")

plaintext = "this is the plaintext"
ciphertext = myEncoder(plaintext)

print(myDecoder(ciphertext) == plaintext) # true
```

Use two different methods:

- `encoder` and `decoder` are functions that return functions
- `encoder` and `decoder` are objects of a class that has a `__call__` method

<center>
**C**
</center>

<center>
(3 points + 1 point)
</center>

Using the [argparse](https://docs.python.org/3/library/argparse.html) library implement a simple note taking
application. The application has only one positional argument:

- `password` will be used as the key to encrypt and decrypt messages

and the following optional arguments:

- `--keywords` or `-k` will be used to add single keywords, this option can be used multiple times
- `--print` or `-p` will print all notes
- `--printany` or `-a` will print only those notes that contain any of the keywords
- `--printall` or `-o` will print only those notes that contain all of the keywords
- `--new` or `-n` will ask the user for the text of a new note with the appropriate keywords
- `--delete` or `-d` will delete a note with a given number

In your implementation:

- store the text of the note in encrypted form, use the functions from the previous exercises
- store the notes in a single file located in the same directory as the script (we will discuss this during class)
- use the `json` module to save the updated list of notes in the same directory as the script
- use a `set` to store the keywords
- apart from the keywords assign the creation date (using `datetime`) to each note and a unique number
- use formatted string literals when printing a note, make sure that the date, number, keywords, and
  note text are displayed in a clear way
- make sure that all the arguments have help information available (using `argparse`)
- make sure that the program has a description information available (using `argparse`)

Extra point: replace the positional argument `password` with an appropriate function from the `getpass` modle. 
Is this safer? Why?

DISCLAMER: This note taking application is only as safe as our implmentation makes it. Use at your own risk! 

<center>
**D**
</center>

<center>
(2 points)
</center>

Next time we will be talking about the `numpy` module.
In preparation please write a script that multiplies two $1024 \times 1024$ matrices. Use python lists and list comprehensions to implement 
the matrices. Measure how much time the script takes to execute. 
