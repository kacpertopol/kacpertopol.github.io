<center>
**MATERIAŁY DODATKOWE**
</center>

W razie kłopotów:

- *Evaluation - Quit Kernel - Local* resetuje jądro mathematici.
  Wszystkie definicje zmiennych, funkcji, ... zostaną usunięte.
- *Evaluation - Abort Evaluation* przerywa aktualnie wykonywane zadanie

Ostatnie twierdzenie Fermata:

- [wiki](https://pl.wikipedia.org/wiki/Wielkie_twierdzenie_Fermata), 
  [youtube](https://youtu.be/qiNcEguuFSA)

Szablony, wzrce: *Help - Wolfram Documentation* i w okienku:

- *guide/Patterns*
- *tutorial/Patterns*

Chaotyczny notebook z zadań (lepiej przyjrzeć się wykładowi profesora):

- [bałagan](---ThisDir---/nof_15_10_2020_zajecia.nb)

Zadanie A:

- proszę dokładnie :-) przyjrzeć się wszystkim rozdziałom dokumentacji  
```
FullSimplify
```

Liczenie objetości bąbelków (proszę zajrzeć równiez do drugiego wykładu profesora):

- [objętość bąbelków](---ThisDir---/nof_15_10_2020_zajecia_1.nb)

Notebooki z zajęć 13 X, aby uruchomić wszystkie komórki wystarczy w menu wybrać *Evaluate* - *Evaluate Notebook*:

- [rano](---ThisDir---/13_10_2022_rano.nb)
- [wieczór 1](---ThisDir---/13_10_2022_wieczor.nb), [wieczór 2](---ThisDir---/13_10_2022_wieczor_1.nb)

<center>
**A**
</center>

<center>
(2 punkt)
</center>

Proszę, z wykorzystaniem funkcji 
```
FullSimplify
```
sprawdzić
czy istnieją liczby całkowite $x$ , $y$ , $z$ oraz $n$, które
spełniają:

- $x^n + y^n = z^n$
- $n > 2$
- $x y z \ne 0$ (żadna z tych liczb nie jest równa 0)

<center>
**B**
</center>

<center>
(1 punkt)
</center>

Proszę skonstruować krótki dowód wyniku z zadania **A**. 
Zeskanowane wyprowadzienie można mi wysłać pocztą elektroniczną.

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Proszę z wykorzystaniem funkcji 
```
If
```
zaimplementować funkcję $f(x , y)$, która przyjmuje wartość $1$
gdy punkt $(x , y)$ wpada w dwu-wymiarowy pierścień 
o zewnętrznym promieniu $1$
oraz wewnętrznym promieniu $\frac{1}{2}$ ze środkiem
w środku układu współrzędnych. W przeciwnym wypadku funkcja przyjmuje wartość $0$.
Proszę tą funkcję narysować z wykorzystaniem
```
RegionPlot
```

<center>
**D**
</center>

<center>
(2 punkt)
</center>

Korzystając z funkcji:
```
Integrate
```
proszę policzyć pole pierścienia z zadania **C**.
Wskazówka: Całka $f(x , y)$ po $x$ oraz $y$ w zakresie od $-1$ do $1$ 
zwróci pole koła. Dlaczego?

<center>
**E**
</center>

<center>
(2 punkt)
</center>

Ciało o masie $1$ kg porusza się po trajektorii $r(t)$ zaimplementowanej jako:
```
(*t - czas w sekundach*)
(*{x , y} - zwracana pozycja w metrach*)
r[t_] := {Cos[t] , Sin[t]};
```
Proszę policzyć jaka siła musi działać na to ciało jeżeli założymy, że porusza się ono zgodnie
z zasadami Newtona. Można w tym celu wykrozystać funkcję:
```
D
```
Proszę skonstruować funkcję, która dla zadanego czasu będzie
zwracała graficzną reprezentację ciała oraz działającej na niego siły.

<center>
**F**
</center>

<center>
(2 punkt)
</center>

Korzystając z funkcji:
```
Import
```
oraz 
```
Cases
```
Proszę napisać program który:

- pobierze ze [strony](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series)
  plik CSV zawierający dane dotyczące liczby potwierdzonych przypadków
  - można skopiować link <https://github.com/CSSEGISandData/COVID-19/raw/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv>
  - wykorzystać go w funkcji 
  ```
  Import
  ```
- zwróci wykres nowych przypadków dla Polski z ostatnich czterech tygodni

<center>
**G**
</center>

<center>
(2 punkt)
</center>

Korzystająć z [definicji pochodnej](https://pl.wikipedia.org/wiki/Pochodna_funkcji) oraz
funkcji:
```
Limit
```
Proszę policzyc pochodne $f'(x)$ następujacych funkcji:

- $f(x) = ln(x)$
- $f(x) = exp(x)$
- $f(x) = x^{2}$

<center>
**H**
</center>

<center>
(2 punkt)
</center>

Korzystając z 
```
Manipulate
```
proszę napisać program, który będzie manipulował
wykresem funkcji $f(x) = exp(x) sin(4 x)$.
Implementacja powinna pozwalać na wykonanie operacji:

- przesunięcia wykresu funkcji w górę lub dół
- przesunięcia wykresu funkcji w lewo lub prawo
- odbicie funkcji względem osi pionowej
- odbicie funkcji względem osi posiomej 
