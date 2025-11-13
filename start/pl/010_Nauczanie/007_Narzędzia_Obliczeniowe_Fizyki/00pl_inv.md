---
title : Narzędzia Obliczeniowe Fizyki
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/0/0b/Ybc7289-bw.jpg?1600959211627)](https://en.wikipedia.org/wiki/File:Ybc7289-bw.jpg)
</center>



# Zawartość:

* [Organizacja](#organizacja)
* [Wykład (prof Jacek Golak)](#wykład-prof-jacek-golak)
* [Zestawy zadań](./000pl_inv.html)
* [Projekty studenckie](./0000pl_inv.html)
* [Zestaw dla grupy 1](#zestaw-dla-grupy-1)



# Organizacja

<center>
**MATHEMATICA**
</center>

Na zajęciach będziemy korzystać z programu Mathematica. Bardzo proszę, 
przed zapoznać się z
[instrukcją instalacji](https://fais.uj.edu.pl/documents/41628/5097967/Oprogramowanie+Mathematica_na_Uniwersytecie_Jagiello%C5%84skim_WFAIS.pdf/e644e1f3-74bb-408e-9f64-529bc329d1e7).
zdobyć licencję i zainstalować program na swoich komputerach. 
Na zajęciach można pracować z własnym laptopem albo z komputerem 
w pracowni. 

**Uwaga**: wszędzie gdzie to konieczne należy wpisywać
uniwersytecki adres e-mail. Licencją objęty jest uniwersytet a e-mail
stanowi metodę weryfikacji, że jesteście państwo studentami uczelni. 
Informacja o aktywacji studenckich kont pocztowych dostępna jest tutaj:

<https://pomocit.uj.edu.pl/poczta_studenci>

w zakładce "Aktywacja kont pocztowych dla studentów i doktorantów".

<center>
**OCENA**
</center>

Na ocenę końcową składać się będą:

- sprawdzian końcowy (30% oceny)
- zadania domowe (35% oceny)
- projekt końcowy (35% oceny)



# Wykład (prof Jacek Golak)

Wykłady profesora Jacka Golaka bedą dostępne na stronie:

<http://users.uj.edu.pl/~golak/>


# [Zestawy zadań](./000pl_inv.html)



# [Projekty studenckie](./0000pl_inv.html)



# Zestaw dla grupy 1

<center>
**MATERIAŁY DODATKOWE**
</center>

- [równania Cauchiego - Riemana](https://en.wikipedia.org/wiki/Cauchy%E2%80%93Riemann_equations)
- [chaotyczny notebook z zajęć](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki/111_Zestaw_dla_grupy_1/nof_13-11-2025_zajecia.nb)

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

