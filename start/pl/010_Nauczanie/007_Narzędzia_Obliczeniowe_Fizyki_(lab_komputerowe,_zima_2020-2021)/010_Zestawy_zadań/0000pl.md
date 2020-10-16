---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Zawartość:

* [Ocenianie](#ocenianie)
* [Zestaw 1 (8 X 2020)](#zestaw-1-8-x-2020)
* [Zestaw 2 (15 X 2020)](#zestaw-2-15-x-2020)



# Ocenianie

- Ćwiczenia można oddawać na każdych zajęciach,
  wystarczy zademonstrować działanie programu oraz króciutko
	o nim opowiedzieć.
- Ćwiczenia z zestawu przypadającego na dane zajęcia
  można oddawać na tych zajęciach lub dwóch kolejnych.
- Ocena z zadań będzie
  wystawiana na podstawie całkowitej ilości
  punktów uzyskanych z rozwiązania ćwiczeń. 




# Zestaw 1 (8 X 2020)

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

- [Hello world!](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/hello.wls)
- [silnia](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/silnia)

Kilka chaotycznych notebooków z zajęć (polecam zaglądnąć najpierw do materiałów profesora Jacka Golaka):

- [pierwszy bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/nof_08_10_2020_A.nb) 
- [drugi bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/nof_08_10_2020_B.nb)

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



# Zestaw 2 (15 X 2020)

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

- [bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/002_Zestaw_2_(15_X_2020)/nof_15_10_2020_zajecia.nb)

Zadanie A:

- proszę dokładnie :-) przyjrzeć się wszystkim rozdziałom dokumentacji  
```
FullSimplify
```

Liczenie objetości bąbelków (proszę zajrzeć równiez do drugiego wykładu profesora):

- [objętość bąbelków](---Thisdir---/nof_15_10_2020_zajecia_1.nb)

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

