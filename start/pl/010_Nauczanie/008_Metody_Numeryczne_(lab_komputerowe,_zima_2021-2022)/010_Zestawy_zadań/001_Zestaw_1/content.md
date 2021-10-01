<center>
**MATERIAŁY DODATKOWE**
</center>

Zachęcam do zapoznania się
z oprogramowaniem do tworzenia wykresów. Ta umiejętność na pewno
przyda się nam na zajęciach. 
Polecam w szczególności, bardzo dojrzały i popularny program [gnuplot](http://www.gnuplot.info/).
Dla osób korzystających z pythona polecam bibliotekę [matplotlib](https://matplotlib.org/),
będącą częścią pakietu [scipy](https://scipy.org/).

<center>
**A**
</center>

<center>
(1 punkt)
</center>

Proszę napisać program rysujący wykres funkcji $sin(x)$ gdzie $-\pi < x \le \pi$.
Można wykorzystać do tego jedną z metod w **MATERIAŁY DODATKOWE**.

<center>
**B**
</center>

<center>
(2 punkt)
</center>

Na zajęciach pokazywałem jak w programie `gnuplot` stworzyć rysunek z trzema wykresami. 
Na górze była cena za BTC, w środku cena ETH a na samym dole, zupełnie bez powodu
wykres funkcji sinus. Proszę, w dowolnym programie, stworzyć porządniejszą wersję tego rysunku. 
Mianowicie:

- zakres danych na osi poziomej (również w przypadku funkcji sinus) powinien objemować czas od 57 do 129 dni
- poziome zakresy wszystkich trzech wykresów powinny się ładnie ze sobą pokrywać
- opis osi poziomej powinien znajdować się jedynie na dolnym wykresie

Do sporządzenia wykresów można wykorzystać [plik z cenami BTC](---ThisDir---/btc.data) oraz
[plik z cenami ETH](---ThisDir---/eth.data). Pierwsza kolumna tych plików zawiera liczbę dni od 01.01.2021
natomiast druga zawiera cenę w USD.

