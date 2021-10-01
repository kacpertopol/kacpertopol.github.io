---
title : Metody Numeryczne
---

<center>
[![](./start/pl/010_Nauczanie/008_Metody_Numeryczne_(lab_komputerowe,_zima_2021-2022)/fortran_punch_card.jpg)](http://www.punctum.com/interest/punch/html/c0133.en.html)
</center>



# Zawartość:

* [Organizacja](#organizacja)
* [Wykład (prof Paweł Góra)](#wykład-prof-paweł-góra)
* [Zestawy zadań](#zestawy-zadań)
	* [Zestaw 1](#zestaw-1)



# Organizacja

<center>
**ZAJĘCIA**
</center>

Zajęcia będą prowadzone w trybie stacjonarnym proszę jednak monitorować 
zarządzenia związane z sytuacją epidemiologiczną. Jeżeli będzie taka
potrzeba zmienimy tryb prowadzenia na zdalny. 

<center>
**OCENA**
</center>

Na każdych zajęciach będzie możliwość oddania zadań z dowolnych poprzednich zestawów.
Zadanie uznaje się za rozwiązane gdy student:

- zademonstruje poprawne działanie swojego programu
- opowie o swojej implementacji

Po zaliczeniu, spakowane do `zip` lub `tar.gz` programy należy wysłać
na <kacper.topolnicki@uj.edu.pl>. Temat wiadomości powinien zawierać ciąg znaków:
"METODYNUMERYCZNE20212022" (brak spacji, duże litery). Archiwum powinno zawierać plik
`README.md` z KRÓTKĄ instrukcją kompilacji oraz uruchomienia.

Ocena z ćwiczeń będzie wystawiona na podstawie liczby punktów otrzymanych za 
rozwiązanie zadań. Konkretna
skala ocen pojawi się pod koniec semestru gdy dostąpmy będzie szerszy rozkład punktów
w grupie.
W przypadku kłopotów będzie możliwość poprawy oceny pisząc projekt końcowy lub
kolokwium - będzie to ustalane indywidualnie z osobami w tarapatach.

Dodatkowo:

- Ćwiczenia można oddawać na każdych zajęciach,
  wystarczy zademonstrować działanie programu oraz króciutko
	o nim opowiedzieć.
- Ćwiczenia z zestawu przypadającego na dane zajęcia
  można oddawać do końca semestru ale ...
  - ... jeżeli pod koniec semestru braknie czasu na zajęciach aby 
    zadanie oddać to nie zostanie ono zalicone 
  - W związku z tym proszę nie zwlekać z oddawaniem zadań.
- Implementacje rozwiązań można pisać w swoim ulubionym języku
  (w ramach rozsądku, proszę wcześniej to ze mną skonsultować -
  muszę być w stanie rozszyfrować wasze rozwiązania) ale:
  - Ideą ćwiczeń jest poznanie algorytmów od podszewki więc
    nie korzystamy z gotowych bibliotek (w razie wątpliwości proszę
	to ze mną skonsultować).
  





# Wykład (prof Paweł Góra)

Wykłady profesora Pawła Góry bedą dostępne na stronie:

<http://th-www.if.uj.edu.pl/zfs/gora/>


# Zestawy zadań



## Zestaw 1

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

Do sporządzenia wykresów można wykorzystać [plik z cenami BTC](./start/pl/010_Nauczanie/008_Metody_Numeryczne_(lab_komputerowe,_zima_2021-2022)/010_Zestawy_zadań/001_Zestaw_1/btc.data) oraz
[plik z cenami ETH](./start/pl/010_Nauczanie/008_Metody_Numeryczne_(lab_komputerowe,_zima_2021-2022)/010_Zestawy_zadań/001_Zestaw_1/eth.data). Pierwsza kolumna tych plików zawiera liczbę dni od 01.01.2021
natomiast druga zawiera cenę w USD.


