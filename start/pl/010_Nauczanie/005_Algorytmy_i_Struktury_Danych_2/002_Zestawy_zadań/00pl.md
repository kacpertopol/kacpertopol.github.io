---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg/1024px-Diagram_for_the_computation_of_Bernoulli_numbers.jpg)](https://en.wikipedia.org/wiki/Algorithm)
</center>



# Zawartość:

* [Zestaw 1](#zestaw-1)
* [Zestaw 2](#zestaw-2)
* [Zestaw 3](#zestaw-3)
* [Zestaw 4](#zestaw-4)



# Zestaw 1

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

Proszę zaimplementować typ danych `dictionarySimple`, będący uproszczoną wersją zbioru, 
posiadającą jedynie trzy operacje:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Tym razem w zbiorze przechowywane będą ciągi znaków o długości $50$. W implementacji
proszę wykorzystać jednowymiarową tablicę, której elementy są ciągami znaków.

Dodatkowo proszę porównać te wyniki do Państwa wyników z **A** oraz **B** i zastanowić się która
implementacja jest lepsza i w jakiej sytuacji. 

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


# Zestaw 2

<center>
**A** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
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
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(4 punkt - implementacja zbioru)
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
Państwa implementację proszę wykorzystać w programie, który bada
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

Korzystając z wyników zadań **A** oraz **B** z zestawu 1
oraz zadania **B** z obecnego zestawu proszę się zastanowić która implementacja
jest lepsza i w jakiej sytuacji. Swoją odpowiedź (popartą odpowiednimi wykresami) proszę przesłać za pośrednictwem e-mail.

Aby ułatwić Państwu zadanie, proszę założyć, że elementami przechowywanymi
we wszystkich zbiorach są słowa składające się z 4 liter (bez polskich znaków).
Można wykorzystać zadanie **A**.

<center>
**UWAGI**
</center>

* Dla każdej implementacji typu danych oraz dla każdej zaimplementowanej operacji proszę dodatkowo:
  * zamieścić w Państwa programie test sprawdzający czy operacje są zaimplementowane prawidłowo
  * aby ułatwic Państwu pracę możemy się umówić, że w teście będzie sprawdzana niewielka ilość
	  przypadków - na tyle mała aby można było je wypisać na ekranie komputera i przeanalizować
* Badając złożoność obliczeniową operacji, proszę się zastanowić jak powina
  wyglądać zależność $t(n)$ czasu wykonania problemu ($t$) od rozmiaru 
	problemu ($n$)
	i nanieść tą hipotezę na odpowiedni wykres. Wystarczy jeden wykres dla wybranej operacji
	w danym problemie.
* Kilka wykresów dla zadania **B** z różną liczbą "klas" albo "porcji" na które może wskazywać funkcja haszująca:
  [1](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh1.pdf), [2](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh2.pdf), [3](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh3.pdf), [4](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh4.pdf), 
  [5](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh5.pdf), [6](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh6.pdf), [7](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh7.pdf), [8](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh8.pdf), 
  [9](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh9.pdf), [10](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh10.pdf), ..., [100](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych_2/002_Zestawy_zadań/002_Zestaw_2/sh100.pdf) 
* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia



# Zestaw 3

<center>
**A** 
</center>

<center>
(2 punkt - implementacja kolejki)
</center>

Proszę zaimplementować typ `priorotyQueue` będący oparty na matematycznym zbiorze
i posiadający, dla słownika $A$ oraz elementu $x$, operacje:

* wstawianie elementu $x$ do kolejki $A$
* zwracanie i jednocześnie usuwanie elementu o najmniejszym "priorytecie" z kolejki $A$

Niech $p(x)$ będzie funkcją zwracającą "priorytet" elementu $x$. Jeżeli w słowniku przechowywane będą liczby 
całkowite, priorytetem może być identyczność - $p(1) = 1$, $p(2) = 2$, ...

Państwa implementację proszę oprzeć na wybranej, omawianej wcześniej, implementacji zbioru. Proszę
zbadać złożoność obliczeniową operacji usuwania z kolejki elementu o najmniejszym "priorytecie" 
(wykres, wartość teoretyczna, dyskusja).

<center>
**B** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(6 punkt - implementacja kolejki)
</center>

Proszę zaimplementować kolejkę priorytetową `priorityQueueBinary` z operacjami jak w zadaniu **A**
ale tym razem proszę oprzeć swoją implementacje o kopiec binarny.  Proszę
zbadać złożoność obliczeniową operacji usuwania z kolejki elementu o najmniejszym "priorytecie" 
(wykres, wartość teoretyczna, dyskusja) oraz porównać wyniki z zadaniem **A**.


<center>
**UWAGI**
</center>

* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 



# Zestaw 4

<center>
**A** 
</center>

<center>
(4 punkt - implementacja grafu)
</center>

Proszę zaimplementować ADT graph, który dla grafu $G$ oraz wierzchołków $x$, $y$ ma implementacje 
następujących operacji:

* $\text{adjacent}(G , x , y)$ - sprawdzanie, czy istnieje krawędź pomiędzy $x$ oraz $y$
* $\text{neighbours}(G , x)$ - zwracja sąsiadów $x$
* $\text{addVertex}(G , x)$ - dodaje $x$ do $G$
* $\text{removeVertex}(G , x)$ - usuwa $x$ z $G$
* $\text{addEdge}(G , x , y)$ - dodaje krawędź pomiędzy $x$ i $y$
* $\text{removeEdge}(G , x , y)$ - usuwa krawędź pomiędzy $x$ i $y$
* $\text{getVertexValue}(G , x)$ - zwraca wartość skojarzoną z $x$
* $\text{setVertexValue}(G , x , v)$ - kojarzy vartość $v$ z wierchołkiem $x$
* $\text{getEdgeValue}(G , x , y)$ - zwraca wartość skojarzoną z krawędzią pomiędzy $x$ oraz $y$
* $\text{setEdgeValue}(G , x , y , v)$ - kojarzy vartość $v$ z krawędzią pomiędzy $x$ oraz $y$

Państwa implementację proszę, na początek, oprzeć ma macierzy połączeń. Dodatkowo proszę zbadać złożoność 
jednej wybranej operacji (wykres oraz opis).

