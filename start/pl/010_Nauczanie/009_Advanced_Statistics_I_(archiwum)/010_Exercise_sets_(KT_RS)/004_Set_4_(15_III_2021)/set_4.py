#!/usr/bin/env python

#@ --- 
#@ title : "additional materials for SET 4"
#@ author : kacper.topolnicki@uj.edu.pl 
#@ institute : ZTUJ, UJ 
#@ --- 
#@  

#@ Simple script to demonstrate the process of extracting 
#@ floating point numbers from a string of characters. Some materials for this tutorial 
#@ were taken from:
#@  
#@ - <https://docs.python.org/3/library/re.html> 
#@ - <https://www.w3schools.com/python/python_regex.asp> 
#@  

#@ # Regular expressions

#@ We begin by importing the "re" module 
#@ref re 
#@ :
#@insert re
#@  
#@ This module contains methods that will allow us to work with regular
#@ expressions (RE). More information on RE can be found 
#@ [**here**](https://docs.python.org/3/library/re.html) or  
#@ [**here**](https://www.w3schools.com/python/python_regex.asp). 
#@  
#@ In order to extract floating point numbers we will use the simple RE `\d+\.\d+`. 
#@ You read this from left to right as: `\d+\.\d+` will match any 
#@ substring of text that starts with a digit (`\d`) repeated one or more 
#@ times (`+`), followed by a period (`\.`), and again followed by a digit (`\d`) 
#@ repeated one or more times (`+`).  
#@  

#@begin re
import re
#@end re

#@ We will be testing this RE on
#@ref teststring 
#@ :
#@insert teststring
#@ First we have to compile the expression 
#@ref compileRE 
#@ :
#@insert compileRE
#@ The result is compiled RE object.
#@ Notice the `r` before `r"\d+\.\d+"`. This notation means "raw string" 
#@ and effects the way python handles backslashes. 
#@  

#@begin teststring 
text = """
1 1.2
this is some text without numbers
this is line number 3
1.2 3.5716
2.1 3.1
Point (1a) from line 233.
"""
#@end teststring 

#@begin compileRE 
floatingPoint = re.compile(r"\d+\.\d+")
#@end compileRE 

#@ Next we will use the compiled RE under `floatingPoint` to look through `text`
#@ and find all substrings that can be interpreted as floating point numbers  
#@ref findall 
#@ :
#@insert findall
#@ 

#@begin findall 
matches = floatingPoint.findall(text)

print(matches)
#@end findall 

#@ Finally we turn all the character strings into numbers
#@ref tofloat
#@ :
#@insert tofloat
#@ Where we map the anonymous lambda function `lambda s : float(s)` over 
#@ each element of the list. The result is a `map object` that needs to be turned 
#@ into a list 
#@ref tolist 
#@ :
#@insert tolist
#@  

#@begin tofloat
floats = map(lambda s : float(s) , matches) 

print(floats)
#@end tofloat 

#@begin tolist
floats = list(floats)

print(floats)
#@end tolist
