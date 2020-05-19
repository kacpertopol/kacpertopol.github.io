<center>
**A** 
</center>

<center>
(1 punkt)
</center>

Prowadzicie Państwo serwis internetowy zapewniający dostęp do gier za pośrednictwem
strumienia danych. Gry są uruchamiane na serwerach w waszej firmie 
i chcecie rozsyłać obraz oraz dźwięk do swoich użytkowników z jak 
najmniejszym opóźnieniem.
Zbadaliście sieć połączeń pomiędzy waszą firmą
oraz komputerami $127$ klientów (jesteście raczkującą firmą)
oraz zapisaliście ją w 
[pliku](---ThisDir---/randgraph). Pierwsze dwie kolumny zawierają
indywidualne numery komputerów (numer $1$ to wasza firma, numery 
$2 \ldots 128$ to komputery klientów) pomiędzy, którymi są połączenia.
Trzecia kolumna zawiera średnie opóźnienie sygnału z danymi 
dla danego połączenia. Aby znaleźć optymalną ścieżkę sygnału z 
danymi od waszej firmy (numerek $1$) do klientów należy skonstruować minimalne drzewo
rozpinające graf połączeń. Proszę korzystając z algorytmu Prima
policzyć takie drzewo. [Wskazówka](https://bradfieldcs.com/algos/graphs/prims-spanning-tree-algorithm/).

<center>
**B** 
</center>

<center>
(1 punkt)
</center>

Proszę znaleźć drzewko z poprzedniego zadania korzystając z algorytmu
Kruskala. Proszę porównać efektywność obydwu algorytmów. 
[Wskazówka](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-using-stl-in-c/)
