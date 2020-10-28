<center>
**METRIAŁY DODATKOWE**
</center>

- [wprowadzenie](https://youtu.be/5PcpBw5Hbwo) do liczb zespolonych
  - nie oglądałem tego wykładu do końca ale Grant Sanderson zazwyczaj doskonale tłumaczy, polecam
- chaotyczne [notatki](---ThisDir---/2020-10-22-Note-17-36.pdf)
  - lepiej zerknąć do wykładu *3Blue1Brown* lub Państwa notatek z matematyki 
- chaotyczny [notebook](---ThisDir---/Notebook.nb)
  - lepiej zerknąć do wykładu *3Blue1Brown* lub Państwa notatek z matematyki 
- pisanie pakietów
  - przykład [pakietu](---ThisDir---/Przyklad.wl)
  - [przykład](---ThisDir---/przyklad_pakiet.nb) wykorzystania
- nagranie prezentacji
  - TODO

<center>
**A**
</center>

<center>
(2 punkt)
</center>

Korzystająć z:
```
NSolve
```
proszę znaleźć wartści $x$ dla których zachodzi:

- $f(x) = 0$, gdzie $f(x) = \frac{\sin{x^{2}}}{x^{2}}$
- $x < 2 \pi$
- $x > 0$

<center>
**B**
</center>

<center>
(2 punkt)
</center>

Korzystając z funkcji
```
Plot
```
oraz opcjonalnych argumentów:
```
GridLines -> ... ,
PlotStyle -> ... ,
Frame -> ... ,
Axes -> ... ,
FrameLabel -> ...
```
Proszę narysować wykres funkcji $f(x)$ z zadania **A**
w przedziale o $0$ do $2 \pi$. Wykres powinien:

- być narysowany czerwoną linią
- zawierać pionowe linie 
  w miejscach gdzie w **A** wyliczono $f(x) = 0$
- zamiast osi posiadać ramkę
- zawiera opis pionowej oraz poziomej osi na ramce

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Proszę wprowadzić definicje dwóch macierzy 
w postaci zagnieżdżonych list:

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

oraz sprawdzić z wykorzystaniem funkcji
```
Dot
```
ile wynoszą [iloczyny macierzy](https://pl.wikipedia.org/wiki/Mno%C5%BCenie_macierzy):

- $A.A$
- $B.B$
- $\left( a_{1} A + b_{1} B \right).\left( a_{2} A + b_{2} B \right)$
- $\left( a_{2} A + b_{2} B \right).\left( a_{1} A + b_{1} B \right)$

gdzie $a_{1}$, $b_{1}$, $a_{2}$, $b_{2}$ są liczbami rzeczywistymi.
Czy można te wyniki wykorzystać do reprezentacji [liczb zespolonych](https://pl.wikipedia.org/wiki/Liczby_zespolone)?
Dlaczego?

<center>
**D**
</center>

<center>
(1 punkt)
</center>

Proszę powtórzyć rachunki z zadania **C** dla macierzy:

$$
A = \left(
\begin{array}{cc}
 1 & 0 \\
 -1 & 1 \\
\end{array}
\right)
$$

$$
B = \left(
\begin{array}{cc}
 1 & 1 \\
 1 & 0 \\
\end{array}
\right)
$$

<center>
**E**
</center>

<center>
(2 punkt)
</center>

Liczenie eksponenty liczby $x$:
$$ 
e^{x}
$$ 
można uogólnić do macierzy 
z wykorzystaniem rozwinięcia
$$
e^{x} = \sum_{k = 0}^{\infty} \frac{x^{k}}{k!} = 1 + x + \frac{1}{2} x^{2} + \frac{1}{6} x^{3} + \ldots
$$
oraz zastępując mnożenie, mnożeniem macierzowym. W Mathematice eksponentę z macierzy można policzyć
wykorzystując:
```
MatrixExp
```

Proszę:

- policzyć $e^{B \phi}$ gdzie $B$ jest macierzą z zadania **C**
- wykorzystując
  ```
  Solve
  ```
  zapisać ten wynik w postaci $a A + b B$ gdzie macierze $A$, $B$ są z zadania **C**
  natomiast $a$, $b$ są nieznanymi liczbami

Jak ten wynik ma się do liczb zespolonych?

<center>
**F**
</center>

<center>
(3 punkt)
</center>

Proszę wykorzystać wzorzec:
```
f[c_][z_] := ...
```
aby zaimplementować funkcję 
$$
f_{c}(z) = z^{2} + c
$$

Następnie, korzystając z wzorca:
```
k[n_][c_] := ...
```
funkcji:
```
Nest
```
oraz implementacji funkcji $f$
proszę zaimplementować funkcję $k_{n}(c)$
która dla danej liczby zespolonej $c$
oraz początkowej liczby zespolonej $z_{0} = 0$
wielokrotnie aplikuje funkcję $f$:

$$k_{1}(c) = f_{c}(z_{0})$$
$$k_{2}(c) = f_{c}(f_{c}(z_{0}))$$
$$k_{3}(c) = f_{c}(f_{c}(f_{c}(z_{0})))$$
$$\ldots$$

Wykorzystując
```
RegionPlot
Abs
```
proszę narysować funkcję $1 / |k_{5}(x + i y)|$ gdzie $-2 < x < 1$ oraz $-1.5 < y < 1$.
Co otrzymujemy? Czy można $1/||$ zastąpić inną funkcją?

<center>
**G**
</center>

<center>
(2 punkt)
</center>

Wykorzystując
```
Limit
```
proszę policzyć granice (WSKAZÓWKA: proszę zajrzeć do dokumentacji ;-) :

- $\lim_{x \rightarrow 0^{+}} \frac{|x|}{\sin x}$
- $\lim_{x \rightarrow 0^{-}} \frac{|x|}{\sin x}$

oraz narysować wykres funkcji $\frac{|x|}{\sin x}$.

<center>
**H**
</center>

<center>
(2 punkt)
</center>

Proszę wykonać zadanie **A** biorąc pochodną funkcji $f(x)$, $f'(x)$, zamiast $f(x)$.

<center>
**I**
</center>

<center>
(2 punkt)
</center>
Wykorzystując
```
DiscretePlot
DiscreteLimit
```
proszę narysować wykres funkcji:
$$
f(k) = \sin(k \pi / 16) / k
$$
, gdzie $k$ jest liczbą całkowitą, oraz znaleźć jej granicę przy $k \rightarrow \infty$.
