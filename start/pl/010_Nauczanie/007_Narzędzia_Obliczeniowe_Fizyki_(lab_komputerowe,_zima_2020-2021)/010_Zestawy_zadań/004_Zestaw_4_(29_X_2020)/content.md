<center>
**A**
</center>

<center>
(2 punkt)
</center>

- Korzystająć z wyniku zadania **E** z zestawu trzeciego proszę uzasadnić:
  $$
  exp(i \phi) = cos(\phi) + i sin(\phi)
  $$ 
  gdzie $\phi$ jest liczbą rzeczywistą. 
- Proszę 
  potwierdzić tą zależność rozwijając
  $exp(i \phi)$ z wykorzystaniem:
  ```
  ComplexExpand
  ```
(Funkcja ta rozwija dowolne wyrażenie zakładając, że wszystkie występujące w niej
niewiadome są rzeczywiste.) oraz wyliczyc ile wynosi:

<center>
**B**
</center>

<center>
(2 punkt)
</center>

Proszę uogólnić zadanie **E** z zestawu trzeciego i z wykorzystaniem
```
MatrixExp
```
policzyć $e^{x A + y B}$ gdzie $x, y$ są liczbami rzeczywistymi. Jak ten wynik ma się
do liczb zespolonych? 

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Korzystająć z równań Cauchiego-Riemana (bez paniki, objaśnię na zajęciach i podam przykład)
oraz 
```
DSolve
```
proszę policzyć funkcję 
$$
sin(x + i y)
$$ gdzie $x , y$ są liczbami rzeczywistymi
przy założeniu, że jest ona analityczna
i znamy jej wartości dla $sin(x + i 0) = sin(x)$. 

Wynik prosze porównać z rozwinięciem $sin(x + i y)$ za pomocą
```
ComplexExpand
```
dla kilku wartości $x$ oraz $y$. Dodatkowo z wykorzystaniem
```
ContourPlot
```
proszę narysować wykres części rzeczywistej oraz urojonej $sin(x + i y)$.

<center>
**D**
</center>

<center>
(4 punkt)
</center>

Zajmiemy się obiektamu typu
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
które nazywamy dodawaniem, mnożeniem, braniem części rzeczywistej oraz braniem części urojonej.

Łatwo się domyślić, że obiekty tego typu mogą reprezentować liczby zespolone. Proszę to
sprawdzić i zdefiniować funkcję 
```
power
```
która dla liczby całkowitej $n$ oraz obiektu typu jak wyżej $z$
```
power[n][z]
```
zwraca potęgę $z^{n}$. Wskazówka: można skorzystać z funkcji 
```
Nest
```
ale przypadek podnoszenia do potęgi $0$ trzeba rozważać osobno.

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

<center>
**E**
</center>

<center>
(2 punkt)
</center>

Korzystając z funkcji 
```
Solve
```
proszę znaleźć współrzędne $(x , y)$ punktów na płaszczyźnie, które
leżą na przecięciu 

- prostej przechodzącej przez punkty $(-1 , 1)$, $(1 , 2)$
- okręgu o środku w $(\frac{1}{2} , \frac{1}{2})$ i promieniu $2$

Dodatkowo proszę tą sytuację narysować (w Mathematica).

<center>
**F**
</center>

<center>
(2 punkt)
</center>

Proszę znaleźć wszystkie pierwiastki równania:

$$
z^{4} + z^{2} + 1 == 0
$$

oraz nanieść rozwiązania na płaszczyznę zespoloną (w Mathematice).
