<center>
**A**
</center>

<center>
(3 punkty)
</center>

Proszę policzyć potencjał elektryczny $U$ we wszystkich punktach $(i = 1 \ldots N , j = 1 \ldots N)$ kratownicy:

<center>
![](---ThisDir---/kratownica.jpg)
</center>

zakładająć: 

- $U_{(1 , 1)} = 0$, 
- każdy opornik ma $1 \Omega$
- pomiędzy $(1 , 1)$ oraz $(N , N)$ przepływa prąd o natężeniu $1 A$ ($1 A$ wpływa do $(1,1)$ i wypływa z $(N , N)$)
- $N$ przybiera różne wartości z zakresu $2 \ldots 100$.

Można do tego podejść na wiele sposobów, ale chciałbym aby Państwo popracowali z macierzami
dlatego proszę ułożyć odpowiedni układ równań macierzowych i rozwiązać go z wykorzystaniem:

```
LinearSolve
```

Wyniki proszę zwizualizować z wykorzystaniem 

```
MatrixPlot
```

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Korzystając z wyników zadania **A** proszę wyznaczyć wartość zastępczą
oporności takiego układu i zbadać jak zmienia się ona z $N$.

<center>
**C**
</center>

<center>
(3 punkty)
</center>

Proszę rozwiązać [problem Hanoi](https://pl.wikipedia.org/wiki/Wie%C5%BCe_Hanoi).
Wszystkie kroki rozwiązania powinny być przedstawione w postaci animacji 
z wykorzystaniem:

```
Graphics
```

oraz:

```
ListAnimate
```

<center>
**D**
</center>

<center>
(2 punkty)
</center>

Macierz:

$$
\left(
\begin{array}{ccc}
 \frac{1}{3} & \frac{1}{3} \left(-1-\sqrt{3}\right) & \frac{1}{3} \left(1-\sqrt{3}\right) \\
 \frac{1}{3} \left(\sqrt{3}-1\right) & \frac{1}{3} & \frac{1}{3} \left(-1-\sqrt{3}\right) \\
 \frac{1}{3} \left(1+\sqrt{3}\right) & \frac{1}{3} \left(\sqrt{3}-1\right) & \frac{1}{3} \\
\end{array}
\right)
$$

obraca wektorem wokół pewnej osi. Proszę znaleźć tą oś.
