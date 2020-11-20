<center>
**MATERIAŁY DODATKOWE**
</center>

- [płaszczyzna](https://mathworld.wolfram.com/Plane.html)
- [dwie płaszczyzny](https://mathworld.wolfram.com/Plane-PlaneIntersection.html)
- [chaotyczne slajdy](---ThisDir---/all.pdf)
- [chaotyczne nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EUX8oe3H3YNBqorS5Gv4MjYBeI8CrButWBguYT8-eOmq5g?e=reCbhb)

<center>
**A**
</center>

<center>
(2 punkty)
</center>

Proszę zdefiniować typ danych opisujący płaszczyznę w przestrzeni
trój wymiarowej

- płaszczyznę powinien określać zestaw (współrzędnych) trzech punktów do niej należących
- wzorzec definiujący ten typ danych powinien sprawdzać czy mamy do czynienia z trzema różnymi
  punktami 

Mając ten typ danych proszę zaimplementować funkcję, która rysyje tą płaszczyznę. Wskazówka,
proszę zajrzeć do dokumentacji:

```
InfinitePlane
```

oraz

```
Graphics2D
```
<center>
**B**
</center>

<center>
(2 punkty)
</center>

Korzystając z typu danych zdefiniowanego w zadaniu **A** proszę napisać funkcję zwracającą
wektor normalny do płaszczyzny. Dodatkowo proszę narysować kilka płaszczyzn oraz
wykorzystująć:
```
Arrow
```
kilka odpowiednich wektorów normalnych mających początek zaczeopiony w tych płaszczyznach.

Proszę zwrócić uwagę, że kolejnośc punktów w typie danych 
z **A** ma znaczenie. 

<center>
**C**
</center>

<center>
(3 punkty)
</center>

Proszę zaimplementować funkcję, która biorąc jako argument typ danych z zadania **A**
zwróci *funkcję*, która:

- pobiera dwie liczby rzeczywiste
- zwraca współrzędne punktu leżącego na płaszczyźnie.

Wzkazówka. Korzystając z funkcji
```
Orthogonalize
```
oraz 
```
Normalize
```
proszę wprowadzić dwu wymiarowy układ współrzędnych na tej płaszczyźnie. 

<center>
**D**
</center>

<center>
(3 punkty)
</center>

Proszę zaimplementować funkcję, która korzystając z typu danych w zadaniu **A**:

- pobierze dwie płaszczyzny
- zwróci *funkcję* pobierającą jedną liczbę rzeczywistą i zwracającą współrzędne
  punktu leżącego na przecięciu tych dwóch płaszczyzn
- proszę sprawdzić czy plaszczyzny nie są przypadkiem równoległe, jeżeli są proszę "rzucić" wyjątek wykorzystująć
```
Throw
```

<center>
**E**
</center>

<center>
(2 punkty)
</center>

Proszę policzyć równanie ruchu dla paciorka o masie $1$ nanizanego na
poziomy pręt. Paciorek porusza się bez tarcia po pręcie i 
jest dodatkowo połączony ze ścianą sprężynką o 
stałej sprężystości $1$.
Rachunek proszę przeprowadzić korzystając z formalizmu Lagrangea 
w Mathematice. Następnie proszę rozwiązać
otrzymane równanie ruchu korzystając z 
```
NDSolve
```
zakładając, że na początku ciało było w pozycji równowagi i miało prędkość początkową
$0.5$. Jednostki masy oraz odległości są dowolne.
