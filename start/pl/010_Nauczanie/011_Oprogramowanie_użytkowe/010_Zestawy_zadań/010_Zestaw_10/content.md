<center>
**A**
</center>

<center>
(4 punkty)
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
**B**
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
proszę narysować funkcję $1 / |k_{5}(x + i y)|$ gdzie $-2 < x < 1$ oraz $-1.5 < y < 1.5$.
Co otrzymujemy? Czy można $1/||$ zastąpić inną funkcją?

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Proszę, korzystając z rozwiązania zadania **B**, stworzyć plik GIF z animacją [zbioru Mandelbrota](https://en.wikipedia.org/wiki/Mandelbrot_set).
Można w tym celu stworzyć tabelkę z rysunkami utworzonymi z wykorzystaniem `RegionPlot`. Każdy rysunek w tabelce może mieć, na przykład,
inną liczbę iteracji. Tabelkę można wyeksportować do pliku GIF wykorzysując `Export`. Proszę spróbować pozmieniać tempo animacji w pliku.
