<center>
**A** 
</center>

<center>
(1 punkt)
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
(1 punkt)
</center>

Proszę zaimplementować kolejkę priorytetową `priorityQueueBinary` z operacjami jak w zadaniu **A**
ale tym razem proszę oprzeć swoją implementacje o kopiec binarny.  Proszę
zbadać złożoność obliczeniową operacji usuwania z kolejki elementu o najmniejszym "priorytecie" 
(wykres, wartość teoretyczna, dyskusja) oraz porównać wyniki z zadaniem **A**.


<center>
**UWAGI**
</center>

* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia
  jeżeli pewne warunki są spełnione. Jakie to warunki?
  * Wskazówka: $\equiv$, $\lt$, $\gt$

