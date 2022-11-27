<center>
**MATERIAŁY DODATKOWE**
</center>

- [notebook](---ThisDir---/plots.nb) Mathematici z przykładami

<center>
**A**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Podać dla jakich liczb $a , b , c , d$ funkcja

$$
f(x) =
\begin{cases}
x^3 - 2 x + 1 & x \in [0 , 1] \\
a + b (x - 1) + c (x - 1)^2 - \frac{1}{2} (x - 1)^3 & x \in [1 , d] \\
\end{cases}
$$

tworzy naturalny splajn kubiczny na przedziale $[0 , d]$.

<center>
**B**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

W każdym przedziale $[x_j , x_{j+1}]$ interpolujemy za pomocą wzoru

$$
y(x) = A(x) f_j + B(x) f_{j + 1} + C(x) \xi^{''}_{j} + D(x) \xi^{''}_{j + 1}
$$

gdzie

$$
A(x) = \frac{x_{j + 1} - x}{x_{j + 1} - x_{j}}
$$

$$
B(x) = \frac{x - x_{j}}{x_{j + 1} - x_{j}}
$$

$$
C(x) = \frac{1}{6} \left(A^{3} - A\right)\left(x_{j + 1} - x_{j}\right)^{2}
$$

$$
D(x) = \frac{1}{6} \left(B^{3} - B\right)\left(x_{j + 1} - x_{j}\right)^{2}
$$

Pokazać, że $y(x_{j}) = f_{j}$, $y(x_{j + 1}) = f_{j+1}$, 
$y''(x_{j}) = \xi''_{j}$, $y''(x_{j + 1}) = \xi''_{j+1}$. 
Żądając ciągłości pierwszej pochodnej $y(x)$ w węzłach, wyprowadzić
układ równań na nieznane wielkości $\xi''_{j}$. 

<center>
**C**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Interpolacja wymierna, algorytm Flootera i Hormanna (wykład 6).

- Pokazać, że w przypadku równoodległych węzłów, wagi ${w_{i}}$ są dane wzorem (33).
- Wyliczyć wagi ${w_{i}}$ dla $n = 65$ węzłów i parametru $d = 3$.
