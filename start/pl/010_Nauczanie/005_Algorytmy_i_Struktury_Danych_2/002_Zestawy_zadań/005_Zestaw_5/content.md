<center>
**A** 
</center>

<center>
(2 punkt)
</center>

Proszę zapoznać się z pakietem [Graphviz](https://graphviz.gitlab.io/). Następnie
korzystając z programu *dot* proszę stworzyć plik *jpg* z grafem:

* zawierającym trzy wierzchołki
* zawierającym połączenia, w obydwu kierunkach, pomiędzy wszystkimi wierzchołkami

Przykładowy [plik z prostrzym grafem](---ThisDir---/smallGraph) oraz [rezultat](---ThisDir---/smallGraph.jpg).
Aby stworzyć obrazek wystarczy w linii komend uruchomić:

```
$ dot -Tjpg smallGraph -o smallGraph.jpg
```

[Tutaj](https://www.graphviz.org/pdf/dotguide.pdf) można znaleźć przewodnik po programie *dot*. 


<center>
**B** 
</center>

<center>
(3 punkt - implementacja grafu)
</center>

Proszę uzupełnić Państwa implementację grafu z poprzedniego zestawu o metodę tworzącą plik,
który może być wykorzystany przez program *dot* do narysowania grafu.

<center>
**C** 
</center>

<center>
(7 punkt - implementacja grafu)
</center>

Proszę zaimplementować ADT graph, posiadający wszystkie operacje z zadania **A** w zestawie 4.
Tym razem proszę wykorzystać reprezentację w której dla każdego wierzchołka przechowywana jest
list sąsiadów. Sprawdzić złożoność obliczeniową wybranej operacji i porównać
z zadaniem **A** zestawu 4.

<center>
**D** 
</center>

<center>
(3 punkt)
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

Proszę się zastanowić jak wykorzystać reprezentację grafową do rozwiązania problemu 
znalezienia minimalnej liczby "faz" sygnalizacji świetlnej na skrzyżowaniu (strzałeczki
oznaczają ulice jednokierunkowe):

<center>
[![](---ThisDir---/ul.jpg)](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)
</center>

Sygnalizacja świetlna w każdej "fazie" powinna zezwalać na ruch przez skrzyżowanie
jedynie tym samochodom, których trajektorie nie będą się przecinać. Aby usprawnić działanie
skrzyżowania, liczba tych etapów powinna być jak najmniejsza. 

Wykorzystując jedną z napisanych przez Państwa implementacji grafów oraz zadanie **A** z poprzedniego
zestawu proszę narysować reprezentację grafową takiego skrzyżowania. 

Wskazówka: proszę zajrzeć na początek [źródła](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406).

<center>
**E** 
</center>

<center>
(3 punkt)
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

Korzystając wyników zadania **D**, proszę napisać
program minimalizujący liczbę "faz" sygnalizacji świetlnej dla tego skrzyżowania.

Wskazówka: proszę zajrzeć na początek [źródła](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406).


