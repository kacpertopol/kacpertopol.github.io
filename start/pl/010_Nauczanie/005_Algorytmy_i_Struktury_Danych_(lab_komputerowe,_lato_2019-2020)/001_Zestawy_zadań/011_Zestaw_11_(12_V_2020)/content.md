<center>
**A** 
</center>

<center>
(1 punkt)
</center>

Średnie czasy przejazdu samochodem pomiędzy polskimi miastami
można odczytać z [tabelki](---ThisDir---/czasy) (dane pochodzą z google maps). W pierwszych
dwóch kolumnach znajdują się miasta a w trzeciej kolumnie
znajduje się czas przejazdu w minutach. Proszę znaleźć
najkrótszy czas przejazdu pomiędzy wszystkimi parami miast.
Wynik powinien być w postaci tabeli, której wiersze oraz kolumny
odpowiadają kolejnym miastom natomiast wartości tabelki 
odpowiadają najkrótszym czasom przejazdu.

*Wskazówka*: proszę skorzystać z [algorytmu Floyda Warszalla](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm).

<center>
**B** 
</center>

<center>
(1 punkt)
</center>

Korzystająć z [tabelki czasów przejazdu](---ThisDir---/czasy) (dane pochodzą z google maps)
proszę znaleźć najszybszą trasę pomiędzy wszystkimi parami miast.
Korzystając z programu *dot* (lub innego programu) oraz [tabelki ze współrzędnymi geograficznymi miast](---ThisDir---/positions)
(pierwsza kolumna zawiera nazwę miasta, druga oraz trzecia kolumna zawiera współrzędne geograficzne)
proszę zaznaczyć na grafie wszystkie miasta oraz najszybsze trasy pomiędzy parami miast (jeden rysunek
dla każdej pary). 

*Wskazówka 1*: proszę skorzystać z [algorytmu Floyda Warszalla](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm).

*Wskazówka 2*: Przykładowy [plik do programu dot](---ThisDir---/example_dot) gdzie 
podane są współrzędne wierzchołków. Wykonanie polecenia `dot -Kfdp -n -Tpng example_dot -o example_dot.png`
powinno skutkować stworzeniem [pliku](---ThisDir---/example_dot.png).
