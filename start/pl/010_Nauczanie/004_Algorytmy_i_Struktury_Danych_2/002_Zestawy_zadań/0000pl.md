---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg)](https://en.wikipedia.org/wiki/Algorithm)
</center>



# Zawartość:

* [Zestaw 0](#zestaw-0)
* [Zestaw 1](#zestaw-1)



# Zestaw 0

<center>
**A** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(2 punkty - implementacja zbioru)
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

<center>
**UWAGI**
</center>

* Implementacje proszę wykorzystać w programach, które badają złożoność obliczeniową poszczególnych operacji.
* Proszę opisać podejście wykorzystane do badania złożoności obliczeniowej.
  Jak wygląda zależność czasu wykonania od rozmiaru problemu. Jak to się ma (czy to się ma) do teoretycznej złożoności obliczeniowej?
* Proszę przetestować działanie wszystkich operacji:
  * wystarczy wyniki testów wypisywać na standardowe wyjście
  * nie trzeba korzystać z systemów do unit testów
* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia
  jeżeli pewne warunki są spełnione. Jakie to warunki?

<center>
**MATERIAŁY DODATKOWE**
</center>

- notacja $O$, uwaga w poniższych linkach dla niektórych przypadków są inne wyniki, 
  proszę się zastanowic, która informacja jest prawidłowa:
  - [geeks for geeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
  - [mathematics stack exchange](https://math.stackexchange.com/questions/761006/big-o-and-function-composition) 
- [prosty przykład](./start/pl/010_Nauczanie/004_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/000_Zestaw_0/set_0.zip)


# Zestaw 1

<center>
**B** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(2 punkty -implementacja zbioru)
</center>

Proszę zaimplementować typ danych `setLinked` reprezentujący
matematyczny zbiór oraz wszystkie operacje z zadania **A**.
Tym razem w implementacji proszę wykorzystać posortowane listy łączone.

<center>
**C**
</center>

<center>
(1 punkt)
</center>

Korzystając z wyników zadań **A** oraz **B** proszę się zastanowić która implementacja
jest lepsza i w jakiej sytuacji. 
Uwaga: to zadanie może być zaliczone pod warunkiem prawidłowego wykonania **A** oraz **B**.

<center>
**D**
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych będący uproszczoną wersją zbioru, 
posiadającą jedynie trzy operacje:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Tym razem w zbiorze przechowywane będą ciągi znaków o długości $50$. W implementacji
proszę wykorzystać jednowymiarową tablicę, której elementy są ciągami znaków.

<center>
**UWAGI**
</center>

* Implementacje proszę wykorzystać w programach, które badają złożoność obliczeniową poszczególnych operacji.
* Proszę opisać podejście wykorzystane do badania złożoności obliczeniowej
  i skonfrontować Państwa wyniki z oczekiwaniami teoretycznymi.
* Proszę przetestować działanie wszystkich operacji:
  * wystarczy wyniki testów wypisywać na standardowe wyjście
  * nie trzeba korzystać z zaawansowanych systemów do unit testów
* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia
  jeżeli pewne warunki są spełnione. Jakie to warunki?

<center>
**MATERIAŁY DODATKOWE**
</center>

- notacja $O$, uwaga w poniższych linkach dla niektórych przypadków są inne wyniki, 
  proszę się zastanowic, która informacja jest prawidłowa:
  - [geeks for geeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/)
  - [mathematics stack exchange](https://math.stackexchange.com/questions/761006/big-o-and-function-composition) 
- [prosty przykład z posortowanymi listami łączonymi](./start/pl/010_Nauczanie/004_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/001_Zestaw_1/set_1.zip)


