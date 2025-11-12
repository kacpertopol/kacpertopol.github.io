<center>
**A**
</center>

<center>
(mnożenie i porównywanie macierzy , reprezentacja liczb zespolonych)
</center>

Proszę sprawdzić czy liczbę zespoloną $x + i y$ ($x$, $y$ to liczby rzeczywiste) można reprezentować
w postaci macierzowej:
$$
x A + y B
$$
gdzie macierze:
$$
A =  \left(
\begin{array}{cc}
 1 & 0 \\
 0 & 1 \\
\end{array}
\right)
$$
$$
B =  \left(
\begin{array}{cc}
 0 & -1 \\
 1 & 0 \\
\end{array}
\right)
$$

Wskazówka: proszę sprawdzić czy liczby zespolone zapisane w ten sposób spełniają [aksjomaty](https://mathworld.wolfram.com/FieldAxioms.html).


<center>
**B**
</center>

<center>
(Solve, MatrixExp , reprezentacja liczb zespolonych)
</center>

Korzystając z reprezentacji liczb zespolonych z zadania **A** proszę sprawdzić czy zachodzi ($\phi$ to liczba rzeczywista):
$$
\exp{i \phi} = \cos{\phi} + i \sin{\phi}
$$

Wskazówka: Pierwszym argumentem `Solve` może być równanie macierzowe.

<center>
**C**
</center>

<center>
(currying, zaawansowane szablony funkcji, reprezentacja liczb zespolonych)
</center>

Zajmiemy się obiektami typu
```
cn[x , y]
```
gdzie $x , y$ są liczbami rzeczywistymi. Dla wyrażeń tego typu zdefiniowane są
operacje
```
plus[cn[x1_ , y1_]][cn[x2_ , y2_]] := cn[x1 + x2 , y1 + y2]
```
```
times[cn[x1_ , y1_]][cn[x2_ , y2_]] := cn[x1 x2 - y1 y2 , x1 y2 + y1 x2]
```
```
re[cn[x_ , y_]] := x
```
oraz
```
im[cn[x_ , y_]] := y
```
które będziemy nazywać dodawaniem, mnożeniem, braniem części rzeczywistej oraz braniem części urojonej.

Łatwo się domyślić, że obiekty tego typu mogą reprezentować liczby zespolone. Proszę to
sprawdzić i zdefiniować funkcję 
```
power
```
która dla liczby całkowitej $n$ oraz obiektu typu jak wyżej `z = cn[a, b]`
```
power[n][z]
```
zwraca potęgę $z^{n}$. Wskazówka: można skorzystać z funkcji 
```
Nest
```

Wiedząc, że 
$$
Re(e^{i \phi}) = cos(\phi)
$$
oraz
$$
Im(e^{i \phi}) = sin(\phi)
$$
proszę policzyć $cos(1)$ oraz $sin(1)$ z wykorzystaniem rozwinięcia eksponenty w szereg
$$
e^{z} = exp(z) = \sum_{k = 0}^{\infty} \frac{z^{n}}{n!}
$$
Proszę szereg obciąć po $100$ wyrazach i skorzystać z własnej implementacji podnoszenia do potęgi.
Wynik proszę porównać z 
```
N[Cos[1]]
```
oraz
```
N[Sin[1]]
```
Wskazówka: `re` oraz `im` można wrzucić pod sumę.

<center>
**D**
</center>

<center>
(DSolve, równania różniczkowe)
</center>

Korzystając z równań Cauchiego-Riemana (bez paniki, objaśnię na zajęciach i podam przykład)
oraz 
```
DSolve
```
proszę policzyć funkcję 
$$
sin(x + i y)
$$ gdzie $x , y$ są liczbami rzeczywistymi
przy założeniu, że jest ona analityczna (z założenia tego wynika, między innymi, że posiada ona pochodne)
i znamy jej wartości dla $sin(x + i 0) = sin(x)$. 

Wynik proszę porównać z rozwinięciem $sin(x + i y)$ za pomocą
```
ComplexExpand
```
dla kilku wartości $x$ oraz $y$. Dodatkowo z wykorzystaniem
```
ContourPlot
```
proszę narysować wykres części rzeczywistej oraz urojonej $sin(x + i y)$.

Wskazówka: oprócz równania różniczkowego cząstkowego w liście równań powinny pojawić się warunki brzegowe.
