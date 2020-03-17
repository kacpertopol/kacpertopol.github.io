---
title : Coronavirus
---

<center>
![](http://i.huffpost.com/gen/1541306/thumbs/o-WALKING-DEAD-POSTER-facebook.jpg)
</center>



# Zawartość:

* [Skype](#skype)
* [Obecności](#obecności)
* [Algebra i Gemetria](#algebra-i-gemetria)
* [Algorytmy i Struktury Danych](#algorytmy-i-struktury-danych)
* [Ewolucja czasowa przewidywań rozwoju epidemii](#ewolucja-czasowa-przewidywań-rozwoju-epidemii)



# Skype

W związku z zarządzeniem Pani Dziekan zajęcia będą prowadzone
za pośrednictwem internetu. Będę dostępny na **Skype** w godzinach
gdy normalnie mielibyśmy zajęcia w budynku WFAIS. Bepośrednio
przed zajęciami na stronie pojawi się link:

<center>
**TU POJAWI SIĘ LINK DO SKYPE BEZPOŚREDNIO PRZED ZAJĘCIAMI**
</center>

który można wykorzystać
aby dołączyć do rozmowy (UWAGA nie wszystkie przeglądarki
są wspierane - Google Chrome powinien działać).

Jeżeli ktoś ma problemy techniczne z połączeniem
to proszę je zgłaszać na <kacper.topolnicki@uj.edu.pl>.
W temacie wiadomości proszę umieścić "SKYPE2020".

<div style="text-align: center"><a href = #zawartość title = "zawartość">↑</a><a href = #obecności title = "obecności">→</a></div>

# Obecności

Z przyczyn technicznych podarujemy sobie sprawdzanie obecności ale
bardzo prosiłbym, w miarę możliwości, pojawiać się na **Skype**
w czasie gdy normalnie mielibyśmy zajęcia.

<div style="text-align: center"><a href = #skype title = "skype">←</a><a href = #zawartość title = "zawartość">↑</a><a href = #algebra-i-gemetria title = "algebra i gemetria">→</a></div>

# Algebra i Gemetria

Dodatkowo do czasu odwołania:

* studenci wysyłają mi zeskanowane zadania na <kacper.topolnicki@uj.edu.pl>,
  w temacie proszę umieścić "ALGEBRA2020"
  * istnieją aplikacje na telefony komórkowe, które pozwalają zdjęcie
    kartki papieru zamienić na ładnie wyglądający dokument PDF - proszę
    się temu przyjrzeć
* moga się zmienić zasady oceniania, proszę monitorować zmiany na stronie


<div style="text-align: center"><a href = #obecności title = "obecności">←</a><a href = #zawartość title = "zawartość">↑</a><a href = #algorytmy-i-struktury-danych title = "algorytmy i struktury danych">→</a></div>

# Algorytmy i Struktury Danych

Proponuję następującą formulę prowadzenia zajęć:

* krótkie omówienie zajęć ($\approx 45$ minut)
* indywidualne konsultacje na **Skype** ($\approx 45$ minut)

Bardzo proszę osoby, które chcą omówić zadania indywidualnie aby 
pozostały dostępne na **Skype** po ogólnym omówieniu zadań.
Mój login **Skype** to *live:kacpertopol*.
Prosiłbym o cierpliwość, na każdych zajęciach będzie kilka osób, z którymi
chciałbym porozmawiać. Gdy przyjdzie Państwa kolej napiszę wiadomość.

Dodatkowo do czasu odwołania:

* moga się zmienić zasady oceniania, proszę monitorować zmiany na stronie


<div style="text-align: center"><a href = #algebra-i-gemetria title = "algebra i gemetria">←</a><a href = #zawartość title = "zawartość">↑</a><a href = #ewolucja-czasowa-przewidywań-rozwoju-epidemii title = "ewolucja czasowa przewidywań rozwoju epidemii">→</a></div>

# Ewolucja czasowa przewidywań rozwoju epidemii

**UWAGA**

Wykresy poniżej to tylko spekulacja, nie należy ich wykorzystywać
do praktycznych celów.

**Równanie logistyczne**

Istnieją dość dobre argumenty sugerujące, że ewolucja epidemii powinna spełniać
[równanie logistyczne](https://en.wikipedia.org/wiki/Logistic_function). Jest 
również świetne [wideo](https://youtu.be/Kas0tIxDvrg) na ten temat.

Rozwiązanie równania logistycznego

$$\frac{d}{d t} n(t) = r n(t) (1 - \frac{n(t)}{k})$$

ma ogólną postać

$$n(t) = \frac{k}{1 + \frac{k - p_{0}}{p_{0}} \exp(-r t)}$$

gdzie $r$ określa tępo geometrycznego wzrostu liczny przypadków $n(t)$ na
początku rozwoju epidemii (czas $t \approx 0$), współczynnik $k$ jest związany z wielkością
populacji natomiast $p_{0}$ jest swobodnym parametrem rozwiązania. 

Zakładając dodatkowo, że epidemia rozpoczęła się w czasie $t_{0}$, czyli dokonując podmiany
$t \rightarrow t - t_{0}$, krzywą logistyczną można dopasować do
[danych JHU CSSE](https://github.com/CSSEGISandData/COVID-19). Współczynnikami dopasowania
są $k$, $p_{0}$ , $r$ oraz $t_{0}$. Poniżej znajdują się wykresy przedstawiające ewolucję
przewidywań opartych na tym dopasowaniu ze zwiększającą się liczbą dostępnych danych.
Na wykresach BF (Best Fit - najlepsze dopasowanie), CF (Confidence Band - pasmo ufności), linia pionowa (piątek 13 III 2020), niebieskie punkty (dane).

**Włochy**

<center>
![](./start/pl/010_Nauczanie/001_Coronavirus/015_Ewolucja_czasowa_przewidywań_rozwoju_epidemii/IT.gif)
</center>

**Niemcy**

<center>
![](./start/pl/010_Nauczanie/001_Coronavirus/015_Ewolucja_czasowa_przewidywań_rozwoju_epidemii/GR.gif)
</center>

**Korea Południowa**

<center>
![](./start/pl/010_Nauczanie/001_Coronavirus/015_Ewolucja_czasowa_przewidywań_rozwoju_epidemii/SK.gif)
</center>

**Japonia**

<center>
![](./start/pl/010_Nauczanie/001_Coronavirus/015_Ewolucja_czasowa_przewidywań_rozwoju_epidemii/JP.gif)
</center>




<div style="text-align: center"><a href = #algorytmy-i-struktury-danych title = "algorytmy i struktury danych">←</a><a href = #zawartość title = "zawartość">↑</a></div>
