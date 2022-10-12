---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Zawartość:

* [Ocenianie](#ocenianie)
* [Zestaw 1](#zestaw-1)
* [Zestaw 2](#zestaw-2)
* [Zestaw 3](#zestaw-3)



# Ocenianie

- Ćwiczenia można oddawać na każdych zajęciach,
  wystarczy zademonstrować działanie programu oraz króciutko
	o nim opowiedzieć.
- Ćwiczenia z zestawu przypadającego na dane zajęcia
  można oddawać do końca semestru ale ...
  - ... jeżeli pod koniec semestru braknie czasu na zajęciach aby 
    zadanie oddać to nie zostanie ono zalicone 
  - W związku z tym proszę nie zwlekać z oddawaniem zadań.
- Ocena z zadań będzie
  wystawiana na podstawie całkowitej ilości
  punktów uzyskanych z rozwiązania ćwiczeń. 




# Zestaw 1

<center>
**MATERIAŁY DODATKOWE**
</center>

Tworzenie skryptu, metoda 1 (prostsza):

- po uruchomieniu programu mathematica należy w menu wybrać:
  *File - New - Package/Script - Wolfram Language Script*
- w nowym okienku mozna wpisać treść programu
- po zakończeniu edycji zapisujemy skrypt i zamykamy okienko 
  (to ważne, Mathematica
  korzysta z mechanizmu uniemożliwiającego jednoczesną edycję
  oraz wykonanie skryptu)
- w terminalu (pod linuxem [tak](https://help.ubuntu.com/community/UsingTheTerminal), pod windows [tak](https://www.wikihow.com/Open-Terminal-in-Windows)) nawigujemy do katalogu gdzie znajduje się skrypt
  i uruchamiamy komendą (pod linux, pod windows jest trochę inaczej - proszę samodzielnie po eksperymentować):
	
  ```bash
	... $ ./nazwa_skryptu.wls
	```

Tworzenie skryptu, metoda 2 (linux ale bardziej uniwersalna w tym systemie):

- otwieramy ulubiony edytor tekstu
- wpisujemy do pliku program
- w pierwszej linijce (tzw linijka "hash bang!", musi być zawsze pierwsza, nad nią nie mogą się znajdować puste linie) dodatkowo dodajemy:
  
  ```bash
  #!/usr/bin/env wolframscript
  ```

- linijka ta informuje system operacyjny, który program 
  powinien być wykorzystany do zinterpretowaniu programu 
  zawartego w skrypcie

- alternatywnie można zamieścić bezpośrednią ścieżkę do programu,
  na moim systemie wygląda ona następująco:

  ```bash
  #!/usr/local/Wolfram/Mathematica/12.1/Executables/wolframscript
  ```

- teraz wystarczy nawigować w terminalu do katalogu zawierającego skrypt, zezwolilć aby nasz skrypt był wykonany:

  ```bash
	... $ chmod +x nazwa_skryptu
	```

- ... i go wykonać:

  ```bash
	... $ ./nazwa_skryptu
	```

- skrype można również wykonać z argumentami, np:

  ```bash
	... $ ./silnia 5
	```

Kilka przykładowych skryptów:

- [Hello world!](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/001_Zestaw_1/hello.wls)
- [silnia](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/001_Zestaw_1/silnia)

Kilka chaotycznych notebooków z zajęć (polecam zaglądnąć najpierw do materiałów profesora Jacka Golaka):

- [pierwszy bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/001_Zestaw_1/nof_08_10_2020_A.nb) 
- [drugi bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/001_Zestaw_1/nof_08_10_2020_B.nb)

<center>
**A**
</center>

<center>
(1 punkt)
</center>

Proszę zainstalować i uruchomić program *Mathematica*.

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Korzystająć z *notebook*a proszę zaimplementować ciąg
liczb Fibonacciego $0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21, \ldots$.

<center>
**C**
</center>

<center>
(2 punkty)
</center>

Korzystając z implementacji z zadania **B** proszę stworzyć
uruchamialny skrypt. Skrypt powinien z linii poleceń pobierać pojedyńczy argument, 
liczbe wyrazów w ciągu Fibonacciego. Państwa program powinien następnie wypisywać na ekranie
odpowiednią liczbę początkowych wyrazów tego ciągu.



# Zestaw 2

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

- [bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/002_Zestaw_2/nof_15_10_2020_zajecia.nb)

Zadanie A:

- proszę dokładnie :-) przyjrzeć się wszystkim rozdziałom dokumentacji  
```
FullSimplify
```

Liczenie objetości bąbelków (proszę zajrzeć równiez do drugiego wykładu profesora):

- [objętość bąbelków](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/002_Zestaw_2/nof_15_10_2020_zajecia_1.nb)

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


# Zestaw 3

<center>
**METRIAŁY DODATKOWE**
</center>

- [wprowadzenie](https://youtu.be/5PcpBw5Hbwo) do liczb zespolonych
  - nie oglądałem tego wykładu do końca ale Grant Sanderson zazwyczaj doskonale tłumaczy, polecam
- chaotyczne [notatki](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/003_Zestaw_3/2020-10-22-Note-17-36.pdf)
  - lepiej zerknąć do wykładu *3Blue1Brown* 
  - ... lub Państwa notatek z matematyki 
- chaotyczny [notebook](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/003_Zestaw_3/Notebook.nb)
  - lepiej zerknąć do wykładu *3Blue1Brown* 
  - ... lub Państwa notatek z matematyki 
- pisanie pakietów
  - przykład [pakietu](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/003_Zestaw_3/Przyklad.wl)
  - [przykład](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/010_Zestawy_zadań/003_Zestaw_3/przyklad_pakiet.nb) wykorzystania

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

