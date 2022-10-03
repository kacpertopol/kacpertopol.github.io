*IMPORTANT: This set is ment for students familiar with python.
Points from these exercises will not be taken into account when
estimating the grading curve. They will only be added to your point total
only if you obtained enough points from the other sets.*

<center>
**A**
</center>

<center>
(2 point)
</center>

Using the publication texts from the previous set:

- compile a list of distinct characters in these texts (this includes the various
  types of whitespaces) and calculate the frequency with which these characters appear in the text 
- truncate the text so that it's length would be a multiple of 2 and compile a list of distinct character
  pairs, calculate their frequency in the text
- truncate the text so that it's length would be a multiple of 3 and compile a list of distinct character
  triplets, calculate their frequency in the text

<center>
**B**
</center>

<center>
(2 points)
</center>

Compile the same type of data as in **A** but this time using python code for the text. 
You can use the sample scripts from the previous sets, but since they contain a lot
of natural language it would be better to grab code from [online repositories](https://github.com/search?l=&o=desc&q=language%3APython&s=stars&type=Repositories).

<center>
**C**
</center>

<center>
(3 points)
</center> 

Use the results of **A** and **B** to calculate the [Shanon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
of these texts

$$H(X) = - \sum_{i = 1}^{N} P(x_{i}) log_{2}(P(x_{i}))$$

where $X$ is a random variable whose $N$ possible values $x_{i}$ are distributed with probability $P(x_{i})$ and

- $x_{i}$ are distinct single characters
- $x_{i}$ are distinct character pairs
- $x_{i}$ are distinct character triplets

Discuss the result.
