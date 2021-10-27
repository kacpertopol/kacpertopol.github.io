<center>
**MATERIAŁY DODATKOWE**
</center>

- [niezbyt efektywny algorytm liczenia rozwinięcia binarnego](---ThisDir---/a.py)
  - informacje `python a.py -h`, uruchamianie na własną odpowiedzialność :-)
- [liczenie normy macierzowej w numpy](---ThisDir---/b.py)
  - informacje `python b.py -h`, uruchamianie na własną odpowiedzialność :-)
- dodatkowe wykłady związane z normami macierzowymi:
  - [cornell](https://www.cs.cornell.edu/~bindel/class/cs6210-f09/lec03.pdf)
  - [mit](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-241j-dynamic-systems-and-control-spring-2011/readings/MIT6_241JS11_chap04.pdf)

<center>
**A**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Znajdź rozwinięcie binarne liczb:

- $\frac{1}{10}$
- $\frac{1}{3}$

<center>
**B**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Niech $||\mathbf{x}||$ będzie normą euklidesową wektora $\mathbf{x} \in \mathbb{R}^{n}$, a $\mathbf{A} \in \mathbb{R}^{n \times n}$
będzie macierzą kwadratową. Normą indukowaną macierzy nazywam wielkość

$$
||\mathbf{A}|| = \underset{||\mathbf{x}|| = 1}{\max} || \mathbf{A} \mathbf{x} || 
$$

Znajdź normy indukowane następujących macierzy:

$$
\left(
\begin{array}{ccc}
 2 & 1 & 0 \\
 1 & 2 & 1 \\
 0 & 1 & 2 \\
\end{array}
\right)
$$

$$
\left(
\begin{array}{cc}
 1 & 1 \\
 0 & 1 \\
\end{array}
\right)
$$

<center>
**C**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Udowodnij, że norma indukowana macierzy ortogonalnej wynosi 1.

<center>
**D**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 3 punkt)
</center>

Definicję normy indukowanej można uogólnić także na macierze niekwadratowe. Znajdź normę macierzy

$$
\left(
\begin{array}{ccc}
 1 & 0 & 1 \\
 0 & 1 & 0 \\
\end{array}
\right)
$$

<center>
**E**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Rozwiązać układ równań

$$
  \begin{cases}
    y + z = 1 \\
    x + y + z = 2 \\
	2 x - z = 0
  \end{cases}
$$

za pomocą eliminacji Gaussa z wyborem elementu podstawowego.

<center>
**F**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Za pomocą metody eliminacji Gaussa znajdź macierz $\mathbf{A}^{-1}$, gdzie:

$$
\mathbf{A} =\left(
\begin{array}{cccc}
 4 & 1 & 0 & 0 \\
 1 & 4 & 1 & 0 \\
 0 & 1 & 4 & 1 \\
 0 & 0 & 1 & 4 \\
\end{array}
\right)
$$
