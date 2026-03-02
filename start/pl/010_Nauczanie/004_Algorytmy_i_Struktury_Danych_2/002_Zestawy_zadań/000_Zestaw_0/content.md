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
