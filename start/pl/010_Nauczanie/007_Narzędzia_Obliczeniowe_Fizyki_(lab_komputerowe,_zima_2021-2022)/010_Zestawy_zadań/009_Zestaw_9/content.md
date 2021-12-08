UWAGA: zestaw jest na 16 XII.

<center>
**MATERIAŁY DODATKOWE**
</center>

- [macierz wymiarowości oraz twierdzenie Buckinghama](https://en.wikipedia.org/wiki/Buckingham_%CF%80_theorem)
- [momenty bezwładności](https://en.wikipedia.org/wiki/List_of_moments_of_inertia)
- [analiza wymiarowa i bomba atomowa](https://youtu.be/_gaCAFcW6OY)
- [notatki](---ThisDir---/notatki.pdf)
  - nagrania nie będzie, bardzo przepraszam (nie nagrał się dźwięk, całe szczęście udało mi się rozwiązać ten problem i mam nadzieję, 
    że następnym razem nie będzie już problemów)

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

<center>
**D**
</center>

<center>
(2 punkty)
</center>

Rozważamy bryły sztywne na płaszczyźnie. 
Zakładamy, że płaskie bryły znajdują się w płaszczyźnie $x$ - $y$ oraz:

- $-1 < x < 1$
- $-1 < y < 1$

Proszę zaimplementować trzy funkcje
zwracające:

- masę bryły
- środek masy bryły
- moment bezwładności bryły

Argumentem wszystkich tych trzech funkcji powinna być funkcja biorąca 
współrzędne na płaszczyźnie i zwracająca gęstość (powierzchniową) bryły.

Wyniki proszę porównać z [wartościami tablicowymi](https://en.wikipedia.org/wiki/List_of_moments_of_inertia) 

Wskazówka: można skorzystać z funkcji `NIntegrate`.

<center>
**E**
</center>

<center>
(2 punkty)
</center>

Proszę wykorzystać zadanie **D** oraz funkcję `DensityPlot`
do narysowania kilku figur oraz zaznaczenia ich środków masy.
W opisie wykresu powinna znaleźć się masa bryły oraz jej 
moment bezwładności względem środka masy.
