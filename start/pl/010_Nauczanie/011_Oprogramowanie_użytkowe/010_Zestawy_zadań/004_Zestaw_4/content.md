<center>
**A**
</center>

<center>
(1 punkt)
</center>

Korzystając z funkcji `Solve` proszę znaleźć wszystkie 
[trójki pitagorejskie](https://pl.wikipedia.org/wiki/Tr%C3%B3jki_pitagorejskie),
których wartości są mniejsze lub równe $200$. Trójki pitagorejskie
to liczby całkowite $x$, $y$, $z$ spełniające równanie pitagorasa $x^{2} + y^{2} = z^{2}$.

<center>
**B**
</center>

<center>
(1 punkt)
</center>

Korzystając z wyniku zadania **A** oraz funkcji `Histogram` proszę narysować histogram
wartości "przyprostokątnych" ($x$, $y$). Szerokość pojedynczego binu histogramu
niech wynosi $10$. Wysokości słupków niech oznacza prawdopodobieństwo trafienia w bin.
Dodatkowo proszę opisać rysunek oraz zmienić kolor słupków na inny niż domyślny.

Wskazówka: mogą się przydać funkcje `Flatten` oraz `ReplaceAll` (pisane w skrócie jako operator `/.`).
Dodatkowo proszę uważnie przeczytać dokumentację funkcji `Histogram`.

<center>
**C**
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
**D**
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
**E**
</center>

<center>
(2 punkt)
</center>

Korzstając z funkcji `NIntegrate` proszę policzyć powierzchnię
dwu wymiarowego pierścienia, którego mniejszy promień wynosi $0.5$
a większy promień $1.0$. Proszę ten pierścień narysować korzystając
z funkcji `DensityPlot`.

Wskazówka: wystarczy policzyć dwu-wymiarową całkę z funkcji `isIn[x , y]`,
która przybiera wartość $1$ gdy $(x , y)$ wpada w pierścień oraz $0$
gdy $(x , y)$ jest poza pierścieniem. Funkcję `isIn` można również wykorzystać
w funkcji `DensityPlot`.

<center>
**F**
</center>

<center>
(1 punkt)
</center>

Proszę przeprowadzić rachunek z zadania **E** wykorzystując `Integrate`. 
Wynik proszę porównać z zadaniem **E** oraz powierzchnią pierścienia policzoną
analitycznie (znamy wzór na powierzchnię koła).

<center>
**G**
</center>

<center>
(1 punkt)
</center>

Na kolejnych zajęciach poznamy podstawy pisania tekstów oraz prezentacji z wykorzystaniem
systemu [LaTeX](https://pl.wikipedia.org/wiki/LaTeX) i będziemy korzystać z 
[Overleaf](https://www.overleaf.com/). Proszę spróbować założyć sobie 
darmowe konto na serwisie [Overleaf](https://www.overleaf.com/).
