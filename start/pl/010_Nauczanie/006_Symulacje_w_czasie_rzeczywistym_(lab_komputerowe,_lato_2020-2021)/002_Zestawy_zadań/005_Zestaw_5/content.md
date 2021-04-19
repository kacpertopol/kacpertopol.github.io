<center>
**MATERIAŁY DODATKOWE**
</center>

- [skrypt](---ThisDir---/race.nb)
  - laboratorium do badania róźnych metod rozwiązywania równań róźniczkowych!
  - wymagania: `python3` , `pygame`
  - podstawowe uruchomienie:
    - `$ python3 race.py`
	- `$ ./race.py` (linux, po nadaniu uprawnień do wykonywania, jeżeli python3 nie jest domyślną wersją należy zmienić `#!`)
  - zapisanie inputu użytkownika (wsad) do `INPUT`:
    - `$ ./race.py -c INPUT`
  - zapisanie trajektorii "dżdżownicy" do `STATE`:
    - `$ ./race.py -t STATE`
	- w pliku `STATE` zapisywany jest cały stan "dżdżownicy", nie tylko jej pozycja na ekranie
  - input (wsad) czytany z pliku `INPUT` zamiast z klawiatury:
    - `$ ./race.py -p INPUT`
  - ryswanie trajektorii zapisanej w `STATE`:
    - `$ ./race.py -d STATE`
  - więcej informacji:
    - `$ ./race.py -h`
  - aby zbadać swoją wersją "dżdżownicy" wystarczy w skrypcie dostarczyc własną wersję `updateState`:
    - argumentem jest stan "dżdżownicy", krok czasowy oraz lista aktualnie naciśniętych klawiszy (wsad)
	- wartością zwracaną jest nowy stan po kroku czasowym
	- więcej szczegółów w komentarzach skryptu
	- zachęcam do majstrowania i wypróbowywania różych metod całkowania równania różniczkowego, aktualne
      podejście nie jest najlepsze

<center>
**A** 
</center>

<center>
(3 punkty)
</center>

Zadania z koralikiem wymagały zaimplementowania skomplikowanego systemu pozwalającego
na łączenie ze sobą segmentów drutu i odpowiednich metod pozwalających między innymi
na umiejscowienie koralika w odpowiednim miejscu odpowiedniego segmentu. 
W tym zadaniu, korzystając z wyników poprzednich zadań ([wax on, wax off](https://youtu.be/SMCsXl9SGgY)),
będzie można dramatycznie uprościć całą zabawę i zapomnieć o druciku. 

Proszę założyć, że koralik ma dwa stopnie swobody - współrzędne na płaszczyźnie:
$$
\vec{r}(t) = (x(t) , y(t))
$$
Podobnie jak wcześniej nadajemy koralikowi pewną prędkość początkową:
$$
\dot{\vec{r}}(0) = (v_{0} , 0)
$$
lub
$$
\dot{\vec{r}}(0) = (0 , v_{0})
$$
oraz pewne położenie początkowe:
$$
\vec{r}(0) = (x_{0} , y_{0})
$$
Zamiast wiązać koralik z położeniem wzdłuż drutu będziemy rozwiązywać równanie różniczkowe:
$$
\ddot{\vec{r}}(t) = \frac{\vec{F}(t)}{m} 
$$
gdzie $m$ to masa koralika natomiast siła działające na koralik $\vec{F}(t)$ zależy
od czasu $t$. $\vec{F}(t) \ne 0$ jedynie gdy koralik porusza się po okręgu,
przybiera ona wtedy wartość i kierunek równy, policzonej w zadaniu **C** z zestawu 2, siły dośrodkowej. 

Proszę powtórzyć zadanie **B** z zestawu 2. Tym razem zapominamy o druciku, bierzemy jedynie siły takie jak
w zadaniu **C** z zestawu 2 i rozwiązujemy równanie różniczkowe jak powyżej wykorzystując jedną z metod omawianych
na wykładzie.

<center>
**B** 
</center>

<center>
(2 punkty)
</center>

Koralik jest teraz samochodem. Promienie okręgów w które był wygięty drut są promieniami skrętu samochodu. 
Dodajemy:

- pedał gazu sprawiający, że na samochód działa stała siła przyspieszająca
- pedał hamulca sprawiający, że na samochód działa stała siła hamująca
- extra: tłumienie jak w zadaniu **A** z zadania czwartego

<center>
**C** 
</center>

<center>
(2 punkty)
</center>

Proszę rozważyć jednowymiarowy oscylator harmoniczny (podobnie jak na wykładzie)  z tłumieniem proporcjonalnym do prędkości.
Proszę rozwiązać odpowiednie równanie różniczkowe stosując metody z wykładu, narysować i porównać
portrety fazowe.
