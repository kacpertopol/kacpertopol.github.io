---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg/1024px-Diagram_for_the_computation_of_Bernoulli_numbers.jpg)](https://en.wikipedia.org/wiki/Algorithm)
</center>



# Zawartość:

* [Zestaw 1 (25 II 2020)](#zestaw-1-25-ii-2020)
* [Zestaw 2 (3 III 2020)](#zestaw-2-3-iii-2020)



# Zestaw 1 (25 II 2020)

<center>
**A** 
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych `setSimple` reprezentujący
matematyczny zbiór oraz operacje
które dla dwóch zbiorów $A$, $B$ realizują:

* sumę zbiorów $A \cup B$
* część wspólną zbiorów $A \cap B$
* różnicę zbiorów $A - B$
* sprawdzanie identyczności zbiorów $A \equiv B$

oraz dla elementu $x$ i zbioru $A$ realizują:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Proszę założyć, że istnieje skończona liczba $N$ możliwych elementów. 
Można sobie na przykład wyobrazić, że wszystkie rozpatrywane przez nas 
zbiory są podzbiorami pewnego 
zbioru $\Omega$ zawierającego $N$ elementów. Dzięki takiemu założeniu
implementacja każdego z rozpytywanych zbiorów może być oparta na 
jednowymiarowej tablicy o rozmiarze $N$.
Każdy index $i = 1 \ldots N$ (lub $i = 0 \ldots N-1$) tej tablicy 
odpowiadałby jednemu z elementów $\Omega$. Wartość przechowywana w 
tablicy pod indeksem $i$ (lub $i - 1$) wskazuje na to czy dany element
należy (np. `true` , `1`) do rozpatrywanego zbioru czy nie (np. `false` , `0`).

Państwa implementację proszę wykorzystać w programie, który bada
złożoność obliczeniową poszczególnych operacji.
Dla każdej z zaimplementowanych operacji program powinien produkować jeden plik,
który może być uruchomiony z wykorzystaniem programu [gnuplot](http://www.gnuplot.info/). 
W wiadomości e-mail proszę
opisać podejście wykorzystane do badania złożoności obliczeniowej
i skonfrontować Państwa wyniki z wartościami teoretycznymi.

<center>
**B** 
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych `setLinked` reprezentujący
matematyczny zbiór oraz wszystkie operacje z zadania **A**.
Tym razem w implementacji proszę wykorzystać posortowane listy łączone.

Podobnie jak w poprzednim zadaniu państwa implementację proszę wykorzystać w programie, który bada
złożoność obliczeniową poszczególnych operacji.
Dla każdej z zaimplementowanych operacji program powinien produkować jeden plik,
który może być uruchomiony z wykorzystaniem programu [gnuplot](http://www.gnuplot.info/). 
W wiadomości e-mail proszę
opisać podejście wykorzystane do badania złożoności obliczeniowej
i skonfrontować Państwa wyniki z wartościami teoretycznymi.

<center>
**C**
</center>

<center>
(1 punkt)
</center>

Korzystając z wyników zadań **A** oraz **B** proszę się zastanowić która implementacja
jest lepsza i w jakiej sytuacji. Swoją odpowiedź proszę przesłać za pośrednictwem e-mail.
Uwaga: to zadanie może być zaliczone pod warunkiem prawidłowego wykonania **A** oraz **B**.

<center>
**D**
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych `dictionarySimple`, będący uproszczoną wersją zbioru, 
posiadającą jedynie trzy operacje:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Tym razem w zbiorze przechowywane będą ciągi znaków o długości $50$. W implementacji
proszę wykorzystać jednowymiarową tablicę, której elementy są ciągami znaków.

Podobnie jak w poprzednich zadaniach państwa implementację proszę wykorzystać w programie, który bada
złożoność obliczeniową poszczególnych metod (lub funkcji).
Dla każdej z zaimplementowanych operacji program powinien produkować jeden plik,
który może być uruchomiony z wykorzystaniem programu [gnuplot](http://www.gnuplot.info/). 
W wiadomości e-mail proszę
opisać podejście wykorzystane do badania złożoności obliczeniowej
i skonfrontować Państwa wyniki z wartościami teoretycznymi.

Dodatkowo proszę porównać te wyniki do Państwa wyników z **A** oraz **B** i zastanowić się która
implementacja jest lepsza i w jakiej sytuacji. Swoją odpowiedź proszę przesłać za pośrednictwem e-mail.

<div style="text-align: center"><a href = #zawartość title = "zawartość">↑</a><a href = #zestaw-2-3-iii-2020 title = "zestaw 2 3 iii 2020">→</a></div>

# Zestaw 2 (3 III 2020)

<center>
**A** 
</center>

<center>
[\[źródło\]](https://doi.org/10.1002/bimj.4710260406)
</center>

<center>
(1 punkt)
</center>

Implementacja zbioru wykorzystująca jednowymiarowe tablice
o skończonym rozmiarze z zadania **A** w zestawie 1 zakłada,
że każdemu elementowi zbioru można przypisać liczbę naturalną
$1 \ldots N$. Proszę zaimplementować funkcje implementujące
takie przyporządkowanie dla zbiorów:

* liczb całkowitych $n , n + 1 , n + 2 , \ldots , m$ gdzie $n < m$
* liczb całkowitych $n , n + 2 , n + 4 , \ldots , m$ gdzie $n < m$
* liter $a , b , c , \ldots , z$, bez polskich znaków ęóąśłżźć 
* dwuliterowych napisów, gdzie każda litera jest z zakresu $a - z$ bez polskich znaków ęóąśłżźć

<center>
**B** 
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych `setHashed` reprezentujący
matematyczny zbiór oraz operacje
które dla dwóch zbiorów $A$, $B$ realizują:

* sumę zbiorów $A \cup B$
* część wspólną zbiorów $A \cap B$
* różnicę zbiorów $A - B$
* sprawdzanie identyczności zbiorów $A \equiv B$

oraz dla elementu $x$ i zbioru $A$ realizują:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Tym razem proszę wykrzystać haszowanie otwarte.

<center>
**C** 
</center>

<center>
(1 punkt)
</center>

Korzystając z wyników zadań **A** oraz **B** z zestawu 1
oraz zadania **B** z obecnego zestawu proszę się zastanowić która implementacja
jest lepsza i w jakiej sytuacji. Swoją odpowiedź proszę przesłać za pośrednictwem e-mail.

Aby ułatwić Państwu zadanie, proszę założyć, że elementami przechowywanymi
we wszystkich zbiorach są słowa składające się z 4 liter (bez polskich znaków).
Można wykorzystać zadanie **A**.

<div style="text-align: center"><a href = #zestaw-1-25-ii-2020 title = "zestaw 1 25 ii 2020">←</a><a href = #zawartość title = "zawartość">↑</a></div>
