Naszym celem będzie stworzenie animacji ilustrującej 
rosnące nasiona, np słonecznika:

<center>
![](---ThisDir---/sunFlower.gif)
</center>

<center>
**A**
</center>

<center>
(2 punkt)
</center>

Pierwszy krok to skonstruowanie funkcji rysującej pojedyncze nasionko.
Załóżmy, że nasiono ma trzy atrybuty:

- współrzędną x
- współrzędną y
- rozmiar nasionka s

Taki obiekt można reprezentować trzy elementową listą:

```
{x , y , s}
```

Proszę zaimplementować funkcję:

```
draw[{x_ , y_ , s_}] := ...
```

zwracającą listę (ewentualnie zagnieżdżoną listę) wyrażeń (`Disk[...]`, `Circle[...]`, `Gray[...]`, ...)
opisującydh rysunek nasiona (narazie nie wrzucamy tej listy jeszcze do `Graphics`). Przykładowo
```
draw[{1.0 , 2.0 , 0.1}]
```
mogłoby zwracać:
```
Circle[{1.0 , 2.0} , 0.1]
```

<center>
**B**
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować funkcję:

```
grow[{x_ , y_ , s_}] := ...
```

zwracającą nową listę atrybutów nasiona. 
Rozmiar nasiona w nowej liście powinien wynosić `mul s`, gdzie `mul = 1.01`
dodatkowo zdefiniowaną zmienną.

<center>
**C**
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować funkcję:

```
expand[{x_ , y_ , s_}] := ...
```

zwracającą nową listę atrybutów nasiona. Tym razem przesuwamy położenie środka nasionka.
Nowe położenie powinno mieć współrzędne `mul x` oraz `mul y`, gdzie $mul$ jest zmienną
zdefiniowaną w zadaniu B.

<center>
**D**
</center>

<center>
(2 punkt)
</center>

Proszę zaimplementować funkcję:

```
rotate[{x_ , y_ , s_}] := ...
```

zwracającą nową listę atrybutów nasiona. Tym razem obracamy nasionko względem
środka układu współrzędnych. Kąt obrotu powininen wynosić $\alpha = 2 \pi \frac{\sqrt{5} - 1}{2}$.
Można wykorzystać funkcję `RotationTransform`. 

<center>
**E**
</center>

<center>
(3 punkt)
</center>

Proszę zaimplementować funkcję:

```
singleIteration[seeds_] := ...
```

gdzie `seeds` jest listą nasionek, np:

```
{{0.01 , 0.0 , 0.01} , {0.02 , 0.01 , 0.013} , ...}
```

a wartość zwracana zawiera dodatkowe nasionko. To dodatkowe nasionko
powstaje z pierwszego nasiona w `seeds` poprzez aplikację wcześniej zdefiniowanych
funkcji `grow`, `expand`, `rotate`.

<center>
**F**
</center>

<center>
(2 punkt)
</center>

Korzystająć z funkcji `Nest` oraz `Graphics` proszę stworyć obrazek z $5$ nasionkami.
Można założyć, że pierwsze nasiono ma atrybuty:

```
{0.01 , 0.0 , 0.12 * 0.01}
```

Pod koniec zajęć spróbujemy to rozszerzyć i stworzyć animację.
