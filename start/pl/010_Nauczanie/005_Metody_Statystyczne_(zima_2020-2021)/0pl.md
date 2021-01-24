---
title : Metody Statystyczne
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Standard_Normal_Distribution.png/800px-Standard_Normal_Distribution.png)](https://en.wikipedia.org/wiki/File:Standard_Normal_Distribution.png)
</center>



# Zawartość:

* [Organizacja](#organizacja)
* [Link do zajęć](#link-do-zajęć)
* [Wykłady (Kacper Topolnicki)](#wykłady-kacper-topolnicki)
* [Ćwiczenia (Vitalii Urbanevych)](#ćwiczenia-vitalii-urbanevych)



# Organizacja

<center>
**TRYB PROWADZENIA ZAJĘĆ**
</center>

Zgodnie z nowym [komunikatem](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/001_Organizacja/komunikat.pdf) zarówno wykład jak i ćwiczenia będą prowadzone
w trybie zdalnym.

<center>
**ZAKRES MATERIAŁU**
</center>

- prawdopodobieństwo w podejściu aksjomatycznym
- właściwości prawdopodobieństwa
- interpretacje prawdopodobieństwa
- zmienne losowe
- rozkłady prawdopodobieństwa
- wielowymiarowe zmienne losowe
- zmiana zmiennych losowych
- estymacja punktowa, przedziałowa
- procesy stochastyczne
- łańcuchy Markova
- rodzaje łańcuchów Markova
- stany stacjonarne
- procesy liczące
- procesy kolejkowe

<center>
**WYKŁAD (Kacper Topolnicki)**
</center>

Wykład będzie prowadzony zdalnie z wykorzystaniem *ZOOM*. Na ocenę z wykładu końcową składać się będą:

- kolokwium końcowe (30% oceny)
- ocena z ćwiczeń (70% oceny)

Kolokwium z zagadnień związanych z wykładem zostanie przeprowadzone podczas ostatnich ćwiczeń, 
będzie ono miało wpływ jedynie na ocenę z wykładu.

<center>
**ĆWICZENIA (Vitalii Urbanevych)**
</center>

Ćwiczenia będą prowadzone zdalnie z wykorzystaniem *ZOOM*.

Przed każdym spotkaniem studenci otrzymają zestaw zadań (będzie on udostępniany na tej stronie). Minimalnym warunkiem zaliczenia jest wykonanie co najmniej dwóch zadań z każdego zestawu. Jednak liczba wykonanych zadań wpłynie na ocenę końcową, więc im więcej zadań zastanie wykonane, tym lepiej. Konkretna skala ocen będzie podana przed końcem semestru.

Zadania zaliczane są podczas trwania zajęć, wystarczy zademonstrować działanie odpowiedniego programu oraz krótko o nim opowiedzieć. Studenci mają możliwość dorobić zadania w domu, ale ono muszą być oddane nie później niż na kolejnych zajęciach. Do wykonania zadania każdy może wybrać dowolny język lub środowisko programistyczne, jednak zabronione jest używanie jakichkolwiek bibliotek i funkcji statystycznych lub pomocniczych.





# Link do zajęć

<center>
**WYKŁAD - ZOOM**
</center>

- link: <https://us02web.zoom.us/j/81066425946?pwd=UGxWdjFRMHZXOXdpcmU4ZG42VXIzdz09>

- Meeting ID: 810 6642 5946

- Passcode: 8kt3fY

<center>
**ĆWICZENIA - ZOOM**
</center>

- link: <https://us02web.zoom.us/j/86822792090?pwd=QlBuOTBtajVSU204ekhBUE5WU0xnZz09>

- Meeting ID: 868 2279 2090

- Passcode: 4P3Zcm


# Wykłady (Kacper Topolnicki)

<center>
**ZAGADNIENIA DO KOLOKWIUM**
</center>

Na kolokwium moga pojawić się następujące zagadnienia:

- aksjomaty prawdopodobieństwa
- twierdzenie Bayesa
- ciągłe zmienne losowe
  - rozkład Cauchiego
    - właściwości, wzór
  - rozkład normalny
    - właściwości, wzór
  - zamiana zmiennych losowych (przypadek 1D)
- estymacja punktowa
  - estymator zgodny
  - estymator nie obciążony
- estymacja przedziałowa
  - przedział ufności
- łańcuchy Markova
  - definicja
  - macierz prawdopodobieństwa
  - czym jest stan stacjonarny, czy zawsze istnieje?
- procesy liczące
  - Bernulli
    - przykład
	- macierz prawdopodobieństw
  - Poisson
    - jak się ma do Bernulliego?
- procesy kolejkowe
  - prawo Little'a
  - klasyfikacja procesów kolejkowych
  - M/M/1
    - podstawowe własności


Jeżeli zadanie na kolokwium będzie wymagać przeprowadzenia obliczeń to będą to BARDZO proste rachunki.
Nie przewiduję skomplikowanych wyprowadzeń.

<center>
**LITERATURA**
</center>

- [*Probability, Random Processes, and Statistical Analysis* Hisashi Kobayashi, Brian L. Mark, William Turin](https://www.cambridge.org/core/books/probability-random-processes-and-statistical-analysis/1909C657E4758038B54C4235B3AD0FDF)
- [*Probability and Statistics for Computer Scientists* Michael Baron](https://www.routledge.com/Probability-and-Statistics-for-Computer-Scientists/Baron/p/book/9781138044487)

<center>
**MATERIAŁY DODATKOWE**
</center>

- [wykład dr hab. prof UJ Romana Skibińskiego](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/RomanSkibinskiWyklad.pdf)
- [instrukcja](https://fais.uj.edu.pl/documents/41628/5097967/OprogramowanieMathematica_na_Uniwersytecie_Jagiello%C5%84skim_2018.pdf/eca91225-a7c0-48fb-94a9-a08553de7fd7) installacji programu Mathematica
  ze [strony](https://fais.uj.edu.pl/dla-studentow/studia-z-mathematica)
  - **UWAGA** wszędzie gdzie to konieczne należy wpisywać uniwersytecki adres e-mail. Licencją objęty jest uniwersytet a e-mail stanowi metodę weryfikacji, że jesteście państwo studentami uczelni. Informacja o aktywacji studenckich kont pocztowych dostępna jest [tutaj](https://pomocit.uj.edu.pl/poczta_studenci) 
    w zakładce “Aktywacja kont pocztowych dla studentów i doktorantów”.


<center>
**wykład 1**
</center>

<center>
(17 X 2020)
</center>

- [slajdy](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/wykład_2020-10-17-Note-11-22.pdf)
- notebooki Mathematici
  - wystarczy uruchomić w mathematice pliki *.nb* i w menu *Evaluation - Evaluate All*
  - instrukcja instalowania Mathematici dla studentów zajduje się w tekście [strony](https://kacpertopol.github.io/000pl.html), 
	  proszę uważnie przeczytać tekst jak również PDF, który jest do ściągnięcia z tej strony
  - [notebook](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/mh.zip) Mathematici z symulacją problemu Montiego Halla (źródło obrazków: [samochód](https://commons.wikimedia.org/wiki/File:Blue_old_car.svg), [koza](https://commons.wikimedia.org/wiki/File:Goat_cartoon_04.svg))
  - [notebook](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/fgp.zip) z rysunkami funkcji gęstości prawdopodobieństwa
- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EfTfTfuFUqZLmpmjoTbBXIsBumimbv9xevBuN4CsBcrlaA?e=w5x3ik) wykładu
  - korzystam z nowego programu, udało się nagrać jedynie mniej więcej połowę, przepraszam :-(
- prawdopodobieństwo obiektywne i subiektywne, Bayesian and frequentist interpretation
  - link pojawi się wkrótce
- problem MH
  - [numberphile na youtube](https://youtu.be/4Lb-6rxZxx0)
  - [dłuższe wyjaśnienie](https://youtu.be/ugbWqWCcxrg)
  - [artykuł na wikipedii](https://en.wikipedia.org/wiki/Monty_Hall_problem)

<center>
**wykład 2**
</center>

<center>
(25 X 2020)
</center>

- nieco mniej chaotyczne [slajdy](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/ms_2.pdf)
- nowe, króciutkie, [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EX1qBOu3wMZMsWNJ-P-RwGsBAachwZlIjVar_SU-cAlSEQ)
  - postanowiłem sporządzić od zera nowe nagranie do "mniej chaotycznych" slajdów
  - jest bardzo krótkie, pomijam wiele obliczeń - proszę je jednak dokładnie prześledzić
- notebooki Mathematici
  - wystarczy uruchomić w mathematice pliki *.nb* i w menu *Evaluation - Evaluate All*
  - instrukcja instalowania Mathematici dla studentów zajduje się w tekście [strony](https://kacpertopol.github.io/000pl.html), 
	  proszę uważnie przeczytać tekst jak również PDF, który jest do ściągnięcia z tej strony	
  - [notebook](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/examples.nb) rozkład normalny 2D
	  - proszę czytać komentarze
  - [notebook](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/examples1.nb) macierz kowariancji oraz zamiana zmiennych w 2D
	  - proszę czytać komentarze
- wyniki eksperymentu:
  - tak na prawdę interesujące są jedynie dwie sytuacje: 
    - $12$ osób uznało, że bardziej prawdopodobna jest stytuacja: Linda jest kasjerką oraz aktywną członkinią ruchu feministycznego
    - $13$ osób uznało, że bardziej prawdopodobna jest sytuacja: Linda jest kasjerką w banku
  - Czy potraficie Państwo uzasadnić dlaczego $12$ osób, czyli prawie połowa osób, się myli?
  - [źródło](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow) eksperymentu
- YouTube
  - jest mnóstwo materiałów, proszę sobie wpisać hasła takie jak "Jacobian", "change of variables"

<center>
**wykład 3**
</center>

<center>
(5 XII 2020)
</center>

- [slajdy](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/wyklad_3.pdf)
- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EdR3X9a13fxNhbFXGGwTI9sBFe_yGXrUM5M15T8yQN8dRg?e=dHChaG)
- [notebook Mathematici](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/05_12_2020.nb)
  - po uruchomieniu w Mathematice wystarczy *Evaluation -> Evaluate Notebook*
- krążyłem wokół tego tematu podczas wykładu ale chyba w końcu nie podałem definicji - czy po wykonaniu ćwiczeń
  potrafią Państwo powiedzieć czym jest stan stacjonarny?

<center>
**wykład 4**
</center>

<center>
(20 XII 2020)
</center>

- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/ERUnK5HhpQRJm6vAz1wvIOMB-dV6CH8OmZU7TyFEcU40iQ?e=I2YRqC) 
- [slajdy](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/20_12_2020.pdf)
- wykład korzystał również z:
  - [rodzaje łańcuchów](http://wwwf.imperial.ac.uk/~ejm/M3S4/NOTES3.pdf)
  - [unikalność rozwiązania](http://www.stat.yale.edu/~jtc5/251/readings/Basics%20of%20Applied%20Stochastic%20Processes_Serfozo.pdf) 
  - [dodatkowy wykład 1](https://mast.queensu.ca/~stat455/lecturenotes/set3.pdf)
  - [dodatkowy wykład 2](https://siamak.isoperimetric.info/teaching/markov/files/equilibrium-2.pdf)
  - [dodatkowy wykład 3](http://math.uchicago.edu/~may/REU2017/REUPapers/Freedman.pdf)
- notebooki Mathematici 
  - [Bernulli](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/20_12_2020.nb)
  - [Markov](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/20_12_2020_1.nb)
  - TODO: Metoda Funkcji Generującej

<center>
**wykład 5**
</center>

<center>
(10 I 2021)
</center>

- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/ESgo0-PppftKt6oLnx4561YBeWm8hRXuTRHnwoLyscFX6w?e=jCgjar)
- [slajdy](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/wyklad_5.pdf)
- [notebook](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/010_Wykłady_(Kacper_Topolnicki)/autocorrelation.nb) Mathematici 
  - wystarczy uruchomić notebook (Evaluate Notebook)
  - TODO - pojawi się uzupełniona wersja z wartościami oczekiwanymi dla procesu liczącego Bernulliego



# Ćwiczenia (Vitalii Urbanevych)

<center>
**zestaw 1**
</center>

<center>
(21 XI 2020)
</center>

- [Plik](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/013_Ćwiczenia_(Vitalii_Urbanevych)/1_Urbanevych_2020.pdf) PDF z zestawem zadań.

<center>
**zestaw 2**
</center>

<center>
(5 XII 2020)
</center>

- [Plik](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/013_Ćwiczenia_(Vitalii_Urbanevych)/2_Urbanevych_2020_new.pdf) PDF z zestawem zadań.

<center>
**zestaw 3**
</center>

<center>
(19 XII 2020)
</center>

- [Plik](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/013_Ćwiczenia_(Vitalii_Urbanevych)/3_Urbanevych_2020_new.pdf) PDF z zestawem zadań.

<center>
**zestaw 4**
</center>

<center>
(9 I 2021)
</center>

- [Plik](./start/pl/010_Nauczanie/005_Metody_Statystyczne_(zima_2020-2021)/013_Ćwiczenia_(Vitalii_Urbanevych)/4_Urbanevych_2020.pdf) PDF z zestawem zadań.


