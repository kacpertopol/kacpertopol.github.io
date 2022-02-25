---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg/1024px-Diagram_for_the_computation_of_Bernoulli_numbers.jpg)](https://en.wikipedia.org/wiki/Algorithm)
</center>



# Zawartość:

* [Zestaw 1](#zestaw-1)



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
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(2 punkty -implementacja zbioru)
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

Podobnie jak w poprzednich zadaniach państwa implementację proszę wykorzystać w programie, który bada
złożoność obliczeniową poszczególnych metod (lub funkcji).
Dla każdej z zaimplementowanych operacji program powinien produkować jeden plik,
który może być uruchomiony z wykorzystaniem programu [gnuplot](http://www.gnuplot.info/). 
W wiadomości e-mail proszę
opisać podejście wykorzystane do badania złożoności obliczeniowej
i skonfrontować Państwa wyniki z wartościami teoretycznymi.

Dodatkowo proszę porównać te wyniki do Państwa wyników z **A** oraz **B** i zastanowić się która
implementacja jest lepsza i w jakiej sytuacji. Swoją odpowiedź proszę przesłać za pośrednictwem e-mail.

<center>
**UWAGI**
</center>

* Dla każdej implementacji typu danych oraz dla każdej zaimplementowanej operacji proszę dodatkowo:
  * zamieścić w Państwa programie test sprawdzający czy operacje są zaimplementowane prawidłowo
  * aby ułatwic Państwu pracę możemy się umówić, że w teście będzie sprawdzana niewielka ilość
	  przypadków - na tyle mała aby można było je wypisać na ekranie komputera i przeanalizować
		ręcznie
* Badając złożoność obliczeniową operacji, proszę się zastanowić jak powina
  wyglądać zależność $t(n)$ czasu wykonania problemu ($t$) od rozmiaru 
	problemu ($n$)
	i nanieść tą hipotezę na odpowiedni wykres. Wystarczy zbadanie złożoności
	obliczeniowej jednej wybranej operacji dla danego problemu.
* Kilka przykładów, w których badana jest złożonosć operacji dodawania elementu
  do zbioru
  * [wykres](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/setSimple.pdf) oraz [skrypt gnuplot](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATAtestAddElementsSetSimple) i [dane do skryptu](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATASS) dla implementacji wykorzystującej tablicę, której elementami są wartości logiczne
  * dwa wykresy [wykres 1](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/setSorted.pdf), [wykres 2](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/setSortedReversed.pdf) 
    oraz dwa skrypty gnuplot [skrypt 1](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATAtestAddElementsSetLinkedSorted), [skrypt 2](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATAtestAddElementsSetLinkedSortedRev) 
    dla posortowanej listy łączonej. Dodatkowo dane do [skrypt 1](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATASLS) oraz [skrypt 2](./start/pl/010_Nauczanie/005_Algorytmy_i_Struktury_Danych/002_Zestawy_zadań/001_Zestaw_1/DATASLSR).
    * dlaczego te wyniki tak dramatycznie się różnią? Proszę dokładnie przeczytać opis wykresów :-)
  * proszę się zastanowić jak ma się dopasowanie do otrzymanych wyników odpowiedniej krzywej do złożonoći
    obliczeniowej
* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia
  jeżeli pewne warunki są spełnione. Jakie to warunki?
    * Wskazówka: $\equiv$, $\lt$, $\gt$


