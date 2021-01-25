#!/usr/bin/env python

#@ ---
#@ title : "csv file import, export"
#@ author : kacper.topolnicki@uj.edu.pl
#@ institute : ZTUJ, UJ
#@ --- 
#@  

#@  
#@ The `numpycsv.py` script contains a demonstration of
#@ of `csv` file creation and export. These types of files  
#@ can be read by spreadsheet programs such as *MS Exel*  
#@ or *LibreOffice Calc*. 
#@  

#@ # Comments 
#@  
#@ The script contains many comments. Any lines that begin 
#@ with the `#` symbol are ignored by python and only
#@ contain additional information for the programmer. 
#@ The script file contains many instances of `#@`, `#@ref`, ... 
#@ These lines are used by an external programm to create
#@ a PDF file, these lines can also be ignored by the programmer. 
#@ 

#@ # Running the script
#@  
#@ To run the script simply navigate to this directory in the terminal and run: 
#@ ``` 
#@ <user> $ python numpycsv.py 
#@ ``` 
#@ Alternatively you can make the script executable and run: 
#@ ``` 
#@ <user> $ ./numpycsv.py 
#@ ``` 
#@ You can also run `ipython` and execute the commands one by one. 
#@  

#@ # Importing the necessary libraries
#@  
#@ First we import the `numpy` library 
#@ref import 
#@insert import 
#@  

#@begin import
import numpy
#@end import

#@ # Creating a `csv` file 
#@  
#@ Next we create a sample `numpy` array using the `asarray` function
#@ref sample  
#@insert sample  
#@ and export this data to `array.csv` 
#@ref export  
#@insert export 
#@ You can try opening this file in a spreadsheet application. 
#@  

#@begin sample  
array = numpy.asarray([[1 , 2 ,3],[4 , 5 , 6],[7 , 8 , 9]])
#@end sample

#@begin export
numpy.savetxt("array.csv" , array , delimiter = ',')
#@end export

#@ # Importing a `csv` file 
#@  
#@ The file we just created can be imported, converted to  
#@ a `numpy` array and stored in a variable 
#@ref imp 
#@insert imp 
#@  

#@begin imp  
readarray = numpy.genfromtxt("array.csv" , delimiter = ",")
#@end imp

#@ We can print the matrix to check if importing succeeded
#@ref print1  
#@insert print1 
#@ Finally, we can cast the elements of the imported array
#@ to the integer type (originally, elements of `array` were integers).
#@ref print2  
#@insert print2  
#@  

#@begin print1 
print(readarray)
#@end print1 

#@begin print2 
print(readarray.astype("int"))
#@end print2
