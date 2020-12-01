<center>
**MATERIAŁY DODATKOWE**
</center>

- [macierz wymiarowości oraz twierdzenie Buckinghama](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem)

<center>
**A**
</center>

<center>
(3 punkty)
</center>

Kolejne zastosowania macierzy...
 
Proszę napisać funkcję, która tworzy macierz wymiarowości.
Funkcja powinna pobierać:

- listę jednostek bazowych (np `{t , m , l}` oznaczające odpowiednio czas, masę oraz odległość)
- listę wielkości fizycznych związanych z danym problemem (pojedyncza wielkość
  może być np w reprezentacji korzystającej z potęg 
  jednostek bazowych `{-2 , 0 , 1}` 
  co można rozszyfrować jako $t^{-2} m^{0} l^{1}$ czyli wymiar przyspieszenia)

Proszę sprawdzić działanie tej funkcji dla problemów:

- oscylacji wahadła matematycznego (interesujące wielkości fizyczne to: okres wahania, masa wahadła , długość wahadła , przyśpieszenie ziemskie)
- ochładzania cieczy z wykorzystaniem kostek lodu (interesujące wielkości fizyczne to: długość charakterystyczna dla kostek lodu, czas , temperatura,
  przewodnictwo cieplne, objętościowe ciepło właściwe)

oraz porównać z [wikipedią](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem).

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Korzystając z wyników zadania **A** oraz funkcji `NullSpace` proszę sprawdzić 
z jakich bezwymiarowych wielkości można skonstruować prawa fizyczne rządzące
obydwoma problemami:

- oscylacji wahadła matematycznego (interesujące wielkości fizyczne to: okres wahania, masa wahadła , długość wahadła , przyśpieszenie ziemskie)
- ochładzania cieczy z wykorzystaniem kostek lodu (interesujące wielkości fizyczne to: długość charakterystyczna dla kostek lodu, czas , temperatura,
  przewodnictwo cieplne, objętościowe ciepło właściwe)

<center>
**C**
</center>

<center>
(1 punkt)
</center>

Proszę rozwiązać ponownie zadanie **B** ale tym razem z wykorzystaniem 
wbudowanej w Mathemaitcę funkcji `DimensionalCombinations`.
