*IMPORTANT: This set is ment for students familiar with python.
Points from these exercises will not be taken into account when
estimating the grading curve. They will only be added to your point total
only if you obtained enough points from the other sets.*

<center>
**Additional Materials**
</center>

- regular expressions
  - [script](---ThisDir---/set_4.py) with a simple example
  - [line by line](---ThisDir---/set_4.pdf) guide to the script

<center>
**A**
</center>

<center>
(3 point)
</center>

Have a look at the [script from the previous set](---ThisDir---/../003_Set_3_(8_III_2021)/set_3.py)
and try to improve it:

- Separating the text from the background (signal from the noise) assumes that the pixel
  values are normally distributed around some mean value. Is this a good assumption?
  Can you make a better one, and improve the de-noising procedure? How / why does the improvement
  increase the quality of the resulting image?
- Add a command line interface.

<center>
**B**
</center>

<center>
(2 points)
</center>

Assemble a collection of your articles or articles by your favorite collaborators.
Extract the raw text from those papers. You can try the following methods

- use the LaTeX source
- use [pdftotext](https://pypi.org/project/pdftotext/)

<center>
**C**
</center>

<center>
(3 points)
</center>

Extract floating point numbers from the texts of the articles in **B**. Use this data
to test [Benford's Law](https://en.wikipedia.org/wiki/Benford%27s_law) 
