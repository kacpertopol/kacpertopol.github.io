#!/usr/bin/env python

#@ ---
#@ title : "simple plots"
#@ author : kacper.topolnicki@uj.edu.pl
#@ institute : ZTUJ, UJ
#@ --- 
#@  

#@  
#@ The `plots.py` script contains some basic examples
#@ of plots that use the `matplotlib` library. The examples 
#@ below are taken from the official `pyplot`  
#@ tutorial ([link](https://matplotlib.org/tutorials/introductory/pyplot.html)). 
#@ Please have a look at this tutorial, what follows is an abridged version. 
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
#@ <user> $ python plots.py 
#@ ``` 
#@ Alternatively you can make the script executable and run: 
#@ ``` 
#@ <user> $ ./plots.py 
#@ ``` 
#@ You can also run `ipython` and execute the commands one by one. 
#@  

#@ # Importing the necessary libraries  
#@  
#@ First we will import the `numpy` library in
#@ref importnumpy 
#@insert importnumpy
#@ and the `pyplot` module from the `matplotlib` library in 
#@ref importpyplot
#@insert importpyplot
#@ Notice that in the second case we will refer to the module using the 
#@ shorthand `plt`.
#@ 

#@begin importnumpy
import numpy
#@end importnumpy

#@begin importpyplot
import matplotlib.pyplot as plt
#@end importpyplot

#@ # Plotting 
#@  

#@ First we will define some functions to plot.
#@ In order to do this we will first create an
#@ array with function arguments. If our function 
#@ is $f$ and has values $f(z)$ and arguments  $z$ then the variable `x`
#@ref funarg 
#@insert funarg 
#@ will contain all
#@ the values of $z$ - all the function arguments. 
#@ In this case the we take $100$ numbers in the 
#@ range from $0$ to $2 \pi$ (`numpy.math.pi`). 
#@ 

#@begin funarg
x = numpy.linspace(0 , 2.0 * numpy.math.pi , 100)
#@end funarg

#@ Next we need function values. First $f = sin$
#@ref sin
#@insert sin
#@ Notice that `x` is an array of function arguments and 
#@ the function `numpy.sin` maps the sine function over  
#@ each element of the array. The result pointed to by `y1`
#@ is also an array. 
#@ We perform similar steps with the cosine function in  
#@ref cos 
#@insert cos 
#@  

#@begin sin
y1 = numpy.sin(x)
#@end sin
#@begin cos
y2 = numpy.cos(x)
#@end cos

#@ It is time for our first plot. We will use the `plt.plot`
#@ (this is an alias for `matplotlib.pyplot`) function 
#@ref first
#@insert first
#@ If you are running this through `ipython` you might have
#@ noticed that nothing happened. This is because we need to  
#@ run the `plt.show` function
#@ref show 
#@insert show 
#@ This should result in a new window with a plot of the sine function. 
#@ Have a look at the controls at the top of the window, they allow 
#@ you to save the plot, zoom, pan, ... 
#@  

#@begin first 
plt.plot(x , y1)
#@end first

#@begin show  
plt.show()
#@end show

#@ Now a slightly more advanced example. We will give labels
#@ to the horizontal (x) and vertical (y) axis. This can
#@ be done via the `plt.xlabel` and `plt.ylabel` functions
#@ref labels 
#@insert labels 
#@  

#@begin labels
plt.plot(x , y1)
plt.xlabel("position")
plt.ylabel("amplitude")
plt.show()
#@end labels 

#@ In the next example we change the width of the line
#@ on the plot (`linewidth`) and the style of the line 
#@ (`linestyle`)
#@ref linestyle
#@insert linestyle
#@ Notice also that we can use LaTeX math notation 
#@ in the labels of the axis. See the `matplotlib` library
#@ documentation for more plotting options (optional 
#@ arguments in python are function arguments in the form
#@ `<option name> = <option value>`).
#@  

#@begin linestyle
plt.xlabel("position")
plt.ylabel('you can use LaTeX $\phi$')
plt.plot(x , y1 , linewidth = 5.0 , linestyle = "--")
plt.show()
#@end linestyle 

#@ We can also plot two functions on one plot. In the example below
#@ref twofunctions
#@insert twofunctions
#@ we plot both the sine function (`y1`) and the cosine function (`y2`).  
#@ The sine function will be drawn with a dashed dotted red line while 
#@ the cosine function will be drawn with a thick dashed line.
#@  

#@begin twofunctions
plt.xlabel("position")
plt.ylabel("amplitude")
plt.title("simple plot")
plt.plot(x , y1 , linestyle = "-." , color = "red")
plt.plot(x , y2 , linewidth = 4.0 , linestyle = "--")
plt.show()
#@end twofunctions

#@ There are other ways of changing the plot properties.
#@ You can use setter functions as in  
#@ref antialiased
#@insert antialiased
#@ Notice that in this case you have to save the plot to a  
#@ variable (`plot`) and apply the `set_antialiased` method
#@ (turns antialiasing on and off)
#@ directly to the plot (`plot[0].set_antialiased(False)`).
#@ We will talk about this in more detail some other time. 
#@  

#@begin antialiased 
plot = plt.plot(x , y1 , "-.")
plot[0].set_antialiased(False)
plt.show()
#@end antialiased 

#@ Another option is to use the `plt.setp` function
#@ref setp 
#@insert setp 
#@ Here we set the line color to red and change the linewidth.
#@ There are two ways to call this function the second method
#@ref alternative 
#@insert alternative 
#@ might be more familiar to users of other plotting software. 
#@  

#@begin setp
lines = plt.plot(x , y1 , x , y2)
plt.setp(lines , color = "r" , linewidth = 3.0)
plt.show()
#@end setp

#@begin alternative
lines = plt.plot(x , y1 , x , y2)
plt.setp(lines , "color" , "r" , "linewidth" , 3.0)
plt.show()
#@end alternative

#@ Plot legends can be added as in 
#@ref legends 
#@insert legends 
#@ In line  
#@ref firstline
#@ the plot is "unpacked" to two variables (`fig` and `ax`).
#@ Next labels are added to the plot (`label = "sin"` and `label` = "cos").
#@ Finally the legend is added and placed in the central upper 
#@ location (`loc = "upper center"`).
#@  

#@begin legends
#@begin firstline 
fig , ax = plt.subplots()
#@end firstline 
ax.plot(x , y1 , label = "sin")
ax.plot(x , y2 , label = "cos")
ax.legend(loc = "upper center" , shadow = False , fontsize = "small")
plt.show()
#@end legends 

#@ Finally we can add annotations to the plot
#@ref annotations 
#@insert annotations 
#@ The annotation will be inserted into coordinates $(1 , 1)$ 
#@ of the plot. There are other options that can set the coordinate system, 
#@ you can for instance give the annotation coordinated in relative coordinates 
#@ where the bottom left of the plot has coordinate $(0 , 0)$ and the top right 
#@ has coordinate $(1 , 1)$. 
#@  

#@begin annotations
plt.plot(x , y1)
plt.annotate('point where x = 1 and y = 1' , xy = (1 , 1))
plt.show()
#@end annotations 


