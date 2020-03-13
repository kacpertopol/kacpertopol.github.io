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
![](---ThisDir---/IT.gif)
</center>

**Niemcy**

<center>
![](---ThisDir---/GR.gif)
</center>

**Korea Południowa**

<center>
![](---ThisDir---/SK.gif)
</center>

**Japonia**

<center>
![](---ThisDir---/JP.gif)
</center>



