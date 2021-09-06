---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cf/Diagram_for_the_computation_of_Bernoulli_numbers.jpg/1024px-Diagram_for_the_computation_of_Bernoulli_numbers.jpg)](https://en.wikipedia.org/wiki/Algorithm)
</center>



# Zawartość:

* [Zestaw 1](#zestaw-1)
* [Zestaw 2](#zestaw-2)
* [Zestaw 3](#zestaw-3)
* [Zestaw 4](#zestaw-4)
* [Zestaw 5](#zestaw-5)
* [Zestaw 6](#zestaw-6)
* [Zestaw 7](#zestaw-7)



# Zestaw 1

<center>
**A** 
</center>

<center>
(1 punkt)
</center>

Proszę zainstalować *GODOT* korzystając z instrukcji na [oficjalnej stronie](https://godotengine.org/) aplikacji.

<center>
**B** 
</center>

<center>
(2 punkt)
</center>

Proszę przyjrzeć się [dokumentacji](https://docs.godotengine.org/en/stable/) i przygotować dwu wymiarową grę
w której moga Państwo:

- tworzyć nowe figury (mają państwo swobodę, mogą to być okręgi, poligony, ...) w w zadanej pozycji na ekranie
- kontrola nad tworzeniem tych obiektów powinna być z posiomu skryptu [GDScript](https://docs.godotengine.org/en/stable/getting_started/scripting/gdscript/gdscript_basics.html)
- zmieniać położenie obiektów w momencie gdy program tworzy nową klatkę animacji

<center>
**C** 
</center>

<center>
(2 punkt)
</center>

Proszę wykonać zadanie **B** ale tym razem w trzech wymiarach.



# Zestaw 2

<center>
**A** 
</center>

<center>
(2 punkty)
</center>

Proszę zaimplementować symulację zabawki:

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/aa/Bead_roller_coaster.jpg/800px-Bead_roller_coaster.jpg)](https://commons.wikimedia.org/wiki/File:Bead_roller_coaster.jpg)
</center>

Dla uproszczenia proszę założyć:

- ograniczamy się do dwóch wymiarów przestrzennych
- mamy tylko jeden koralik
- mamy jedynie jeden drut
- koralik porusza się wzdłóż drutu bez tarcia
- nie mamy siły grawitacji

Powinna istnieć możliwość poskładania drutu z
segmentów w postaci:

<center>
![](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/002_Zestaw_2/segment.jpg)
</center>

gdzie $x$ oraz $y$ są poziomo oraz pionowo skierowanymi wektorami,
natomiast $r$ jest promieniem okręgu. 
Symulacja powinna dawać możliwość przesuwania paciorka
w dowolne miejsce drutu.

<center>
**B** 
</center>

<center>
(2 punkty)
</center>

Nadajemy paciorkowi z **A** pewną stałą prędkość 
w momencie gdy zostaje on nanizany na drut.
Proszę uzupełnić symulację tak aby w każdej klatce
rysowana była aktualna pozycja paciorka.

<center>
**C** 
</center>

<center>
(2 punkty)
</center>

Proszę uzupełnić symulację tak aby w każdej klatce
rysowany był wektor siły jaka działa na paciorek (może być to strzałeczka,
można również odpowiednio zmieniać kolor paciorka).

<center>
**D** 
</center>

<center>
(2 punkty)
</center>

Teraz paciorek koże również obracać się wzdłów osi 
wyznaczonej przez kierunek drutu. Proszę odpowiednio
uzupełnić swoją symulację tak aby wydoczny był obrót
koralika.


# Zestaw 3

<center>
**A** 
</center>

<center>
(2 punkty)
</center>

W zadaniu **C** z zestawu 2 proszę policzyć siły na kilka sposobów:

- bezpośrednio, korzystając z wzoru na przyspieszenie dośrodkowe
- korzystając z przybliżeń "backward", "forward" oraz "centered" podanych na wykładzie

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Zmieniając krok czasowy, proszę zbadać różnice w czterech podejściach z zadania **A**
poprzez nanienienie na jeden wykres zależności długości siły od czasu.
Jakie wartości kroku czasowego są najbardziej interesujące z perspektywy
silnika gier?

<center>
**C**
</center>

<center>
(3 punkty)
</center>

Korzystając z metody Eulera proszę zaimplementować prostą zabawkę:

- dwu-wymiarowe piłeczki (masa $m$, promień $r$) pojawiają się przy górnej krawędzi
  kwadratowego pudła (długość boku $L$)
- w układzie działa siła grawitacji (przyspieszenie ziemskie $g$)
- odbijając się od śnianek pudła piłeczki tracą ustaloną część swojej energii kinetycznej ($f$)

Proszę zbadać działanie takiej symulacji od ilosci piłeczek $N$. Czy rachunki związane z 
algorytmem Eulera opłaca się wykonywać w głównej pętli gry
czy w pętli silnika fizyki? Jak wygląda sytuacja jeżeli na ekranie będą rysowane jedynie wybrane piłeczki?


# Zestaw 4

<center>
**MATERIAŁY DODATKOWE**
</center>

- [notebook Mathematici](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/004_Zestaw_4/wire.nb) z przykładem
  - wystarczy uruchomić "Evaluate Notebook"
  - proszę zwrócić uwagę na komentarze
- koralik poruszający się po drucie gdy krok czasowy jest odpowiednio mały 
  (ciekawsza jest sytuacja w której rozwiązanie numeryczne eksploduje):

<center>
![](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/004_Zestaw_4/wire_ok.gif)
</center>

<center>
**A** 
</center>

<center>
(2 punkty)
</center>

Koralikowi z poprzedniego zestawu nadajemy pewną prędkość początkową $v(0)$ skierowaną wzdłuż drutu
oraz zakładamy, że na początku znajdował się w pozycji $x(0)$, gdzie $x$ oznacza długość przebytej drogi
wzdłuż drutu.
Proszę, korzystając z jawnego algorytmu Eulera z krokiem czasowym $\Delta t$ (ustawienia silnika fizyki) policzyć położenie koralika jeżeli 
poddany jest on tłumieniu w postaci:

$$ \frac{d v}{d t}(t) = -k v(t) $$

Proszę tak zmieniać wartości $\Delta t$ oraz $k$ aby zaobserwować niestabilność systemu. Sytuację proszę zilustrować animacją.

<center>
**B**
</center>

<center>
(4 punkty)
</center>

Proszę zbadać omawiane na wykładzie metody poprawy stabilności oraz alternatywne algorytmy w kontekście zadania **A**.




# Zestaw 5

<center>
**MATERIAŁY DODATKOWE**
</center>

- laboratorium do badania róźnych metod rozwiązywania równań róźniczkowych!
  - [skrypt](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/005_Zestaw_5/race.py)
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
  - skrypt liczty fizykę w takim samym tempie jak rysowane są na ekranie klatki animacji (maksymalnie 60 fps)
    - zachęcam do modyfikacji skyptu w celu oddzielenia procedur liczących fizykę od procedur zajmujacych się animacją
- [zapisywanie plików tekstowych w GODOT](https://www.reddit.com/r/godot/comments/ghxlan/save_plain_text_to_a_file/)

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


# Zestaw 6

<center>
**MATERIAŁY DODATKOWE**
</center>

- geometria
  - kompendium [**MathWorld**](https://mathworld.wolfram.com/)
    - [liczenie odległości punktu od prostej 2D](https://mathworld.wolfram.com/Point-LineDistance2-Dimensional.html)
    - [liczenie odległości punktu od prostej 3D](https://mathworld.wolfram.com/Point-LineDistance3-Dimensional.html)
    - [liczenie przecięcia dwóch płaszczyzn](https://mathworld.wolfram.com/Plane-PlaneIntersection.html)
    - [liczenie przecięcia linii prostej i płaszczyzny](https://mathworld.wolfram.com/Line-PlaneIntersection.html)
    - ... dość dobre źródło informacji, bardzo wiele dziedzin matematyki - zachęcam do rzucenia okiem
  - krótki [notebook](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/006_Zestaw_6/geom1.nb) z zajęć oraz [pdf](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/006_Zestaw_6/geom1.pdf)
    - liczenie wektorów normalnych
- propozycje projektów
  - [miniaturowy golf](https://en.wikipedia.org/wiki/Miniature_golf)
    - minimalistyczne podejście
    - przeszkody w postaci ścianek z wielokątów
    - wizualizacja w 3D ale fizyka liczona w 2D
  - [jedna z odmian bilarda](https://en.wikipedia.org/wiki/Cue_sports)
    - minimalistyczne podejście
    - wizualizacja w 3D ale fizyka liczone w 2D
    - gra powinna podpowiadać graczowi jakie będą skutki potencjalnego uderzenia kijem 
  - [asteroidy](https://en.wikipedia.org/wiki/Asteroids_(video_game)) ale w 3D
    - minimalistyczne podejście
    - gra odbywa się w pudle o ustalonych rozmiarach
    - można założyć periodyczne warunki (prawa ścianka pudła utożsamiona jest z lewą, górna z dolną, przednia z tylną)
    - asteroidy w postaci zlepków sfer
    - fizyka oraz wizualizacja w 3D
  - dobór naturalny na szalce Petriego
    - lepiej pogadać o tym, proszę o kontakt
    - fizyka w 2D, wizualizacja w 3D

<center>
**A** 
</center>

<center>
(3 punkty)
</center>

Zapominamy kompletnie o druciku i pozwalamy aby koralik poruszał się swobodnie
(wsad nadaje mu odpowiednie przyspieszenie, promień skrętu, hamowanie).
Dodajemy drugi koralik na który działa siła wyłącznie w momencie 
zderzenia z pierwszym koralikiem. Proszę, korzystając z metod omawianych na wykładzie,
zaimplementować taki system.

<center>
**B** 
</center>

<center>
(3 punkty)
</center>

Do systemu włączamy "ściany" od których mogą się odbijać koraliki.
Każda ściana składa się z prostych odcinków muru, stanowi wielobok.
Proszę, korzystając z metod omawianych na wykładzie,
zaimplementować taki system.


<center>
**C** 
</center>

<center>
(1 punkty)
</center>

Proszę zaproponować temat projektu końcowego.


# Zestaw 7

<center>
**0**
</center>

Rozpoczynamy systematyczną powtórkę przed egzaminem. Na każdych kolejnych zajęciach 
będą omawiane "Pytania do egzaminu". Poszczególne pytania będą przypisane 
konkretnym osobom do krótkiego zreferowania podczas zajęć. 

<center>
**A** 
</center>

<center>
(2 punkty)
</center>

Proszę, w ulubionym języku programowania, zaimplementować własną klasę kwaternionów.
Klasa powinna być wyposażona w takie metody aby było możliwe zademonstrowanie równoważności
kwaternionowej oraz macierzowej reprezentacji obrotów w trzech wymiarach. 


<center>
**B** 
</center>

<center>
(2 punkty)
</center>

Proszę, dowolną metodą, oszacować środek masy oraz tensor momentu bezwładności oscypka:

![](./start/pl/010_Nauczanie/006_Symulacje_w_czasie_rzeczywistym_(lab_komputerowe,_lato_2020-2021)/002_Zestawy_zadań/007_Zestaw_7/oscypek.jpg)

Można założyć, że gęstość $\rho$ jest w przybliżeniu równa gęstości wody.



<center>
**C** 
</center>

<center>
(4 punkty)
</center>

Proszę zaimplementować symulację oscypka. Powinna istnieć możliwość zadania dowolnych parametrów początkowych
oraz możliwość interaktywnego przykładania siły do jednego z czubków oscypka. Symulację proszę wykonać w dwóch 
wersjach, przy czym jedna z nich powinna korzystać z kwaternionowej reprezentacji obrotów. 



