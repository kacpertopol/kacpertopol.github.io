<center>
**A** 
</center>

<center>
(1 punkt)
</center>

<center>
[[źródło](https://bradfieldcs.com/algos/)]
</center>

Bierzemy udział w grze, która ma następujęce reguły:

* startuje się z czteroliterowego wyrazu w języku polskim, na przykład "ster"

* gra składa się z iteracji, w każdej iteracji można zmienić jedną literę czteroliterowego wyrazu
  ale pod warunkiem, że orzymane słowo istnieje w słowniku języka polskiego

* gra kończy się gdy w wynku tych transformacji otrzyma się pewne, z góry ustalone słowo końcowe, 
  na przykład "atom"

* wygrywa osoba, która zamieni słowo startowe na słowo końcowe za pomocą najmniejszej liczny
  operacji

Jeżeli za słowo startowe wybierze się "ster" a za końcowe "atom" gra może wyglądać następująco:

```
ster -> step -> stop -> utop -> utom -> atom
```

Proszę zaimplementować program, szukający najkrótszej ścieżki pomiędzy 
zadanym słowem startowym i końcowym.

Wskazówka: Proszę zajrzeć do źródła. 
Słownik języka polskiego, w postaci spakowanego pliku tekstowego, 
można pobrać [tutaj](https://sjp.pl/slownik/growy/).

<center>
**B** 
</center>

<center>
(1 punkt)
</center>

<center>
[[źródło](https://bradfieldcs.com/algos/)]
</center>

Robimy naleśniki. Składniki są następujące:

* $1$ jajko

* $1$ łyżka oleju

* $\frac{3}{4}$ szklanki mleka

* $1$ szklanka proszku do naleśników

* syrop klonowy

* patelnia

Abu zrobić naleśniki należy:

* nagrzać patelnię 

* zmieszać jajko, olej, mleko i proszek do naleśników

* wylać część ciasta naleśnikowego na gorącą patelnię 

* gdy naleśnik jest rumiany od spodu należy przewrócić i podpiec z drugiej strony

* podgrzać syrop klonowy

* zjeść rumiany (z obydwu stron) naleśnik polany ciepłym syropem klonowym

Proszę zareprezentować ten proces w postaci grafu $G$. Następnie proszę napisać
program, który na podstawie grafu $G$ decyduje o kolejności wykonywanych czynności kulinarnych.
Proszę uogólnić swój program, tak aby przyjmował dowolny graf $G$.

Wskazówka: źródło.
