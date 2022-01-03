<!---
<center>
**ZAGADNIENIA DO KOLOKWIUM**
</center>

Na kolokwium mogę pojawić się następujące zagadnienia:

- aksjomaty prawdopodobieństwa
- twierdzenie Bayesa
- ciągłe zmienne losowe
  - rozkład Cauchiego
    - właściwości, funkcja gęstości prawdopodobieństwa
  - rozkład normalny
    - właściwości, funkcja gęstości prawdopodobieństwa
  - zamiana zmiennych losowych (przypadek 1D)
- estymacja punktowa
  - estymator zgodny
  - estymator nie obciążony
- estymacja przedziałowa
  - przedział ufności
- łańcuchy Markova
  - definicja
  - macierz prawdopodobieństwa, grafy procesu
  - czym jest stan stacjonarny, czy zawsze istnieje?
- procesy liczące
  - Bernulli
    - przykład
	- macierz prawdopodobieństw
  - Poisson
    - jak się ma do Bernulliego?
- procesy kolejkowe
  - prawo Little'a
  - klasyfikacja procesów kolejkowych (M/M/1, G/M/1, ...)
  - M/M/1
    - podstawowe własności

Jeżeli zadanie na kolokwium będzie wymagać przeprowadzenia obliczeń to będą to BARDZO proste rachunki.
Nie przewiduję skomplikowanych wyprowadzeń. Kolokwium pisane jest na karteczkach przy włączonych kamerach. 
Po ukończeniu będzie należało karteczki zeskanować / sfotografować i przesłać na <kacper.topolnicki@uj.edu.pl>.
Czas trwania to około $30$ minut.
--->

<center>
**LITERATURA**
</center>

- [*Probability, Random Processes, and Statistical Analysis* Hisashi Kobayashi, Brian L. Mark, William Turin](https://www.cambridge.org/core/books/probability-random-processes-and-statistical-analysis/1909C657E4758038B54C4235B3AD0FDF)
- [*Probability and Statistics for Computer Scientists* Michael Baron](https://www.routledge.com/Probability-and-Statistics-for-Computer-Scientists/Baron/p/book/9781138044487)

<center>
**MATERIAŁY DODATKOWE**
</center>

<!---- [wykład dr hab. prof UJ Romana Skibińskiego](---ThisDir---/RomanSkibinskiWyklad.pdf)--->
- [instrukcja](https://fais.uj.edu.pl/documents/41628/5097967/OprogramowanieMathematica_na_Uniwersytecie_Jagiello%C5%84skim_2018.pdf/eca91225-a7c0-48fb-94a9-a08553de7fd7) installacji programu Mathematica
  ze [strony](https://fais.uj.edu.pl/dla-studentow/studia-z-mathematica)
  - **UWAGA** wszędzie gdzie to konieczne należy wpisywać uniwersytecki adres e-mail. Licencją objęty jest uniwersytet a e-mail stanowi metodę weryfikacji, że jesteście państwo studentami uczelni. Informacja o aktywacji studenckich kont pocztowych dostępna jest [tutaj](https://pomocit.uj.edu.pl/poczta_studenci) 
    w zakładce “Aktywacja kont pocztowych dla studentów i doktorantów”.


<center>
**wykład 1**
</center>

- [slajdy z zeszłego roku](---ThisDir---/wykład_2020-10-17-Note-11-22.pdf)
- notebooki Mathematici
  - wystarczy uruchomić w mathematice pliki *.nb* i w menu *Evaluation - Evaluate All*
  - instrukcja instalowania Mathematici dla studentów zajduje się w tekście [strony](https://kacpertopol.github.io/000pl.html), 
	  proszę uważnie przeczytać tekst jak również PDF, który jest do ściągnięcia z tej strony
  - [notebook](---ThisDir---/mh.zip) Mathematici z symulacją problemu Montiego Halla (źródło obrazków: [samochód](https://commons.wikimedia.org/wiki/File:Blue_old_car.svg), [koza](https://commons.wikimedia.org/wiki/File:Goat_cartoon_04.svg))
  - [notebook](---ThisDir---/fgp.nb) z rysunkami funkcji gęstości prawdopodobieństwa
- prawdopodobieństwo obiektywne i subiektywne, Bayesian and frequentist interpretation
  - link pojawi się wkrótce
- problem MH
  - [numberphile na youtube](https://youtu.be/4Lb-6rxZxx0)
  - [dłuższe wyjaśnienie](https://youtu.be/ugbWqWCcxrg)
  - [artykuł na wikipedii](https://en.wikipedia.org/wiki/Monty_Hall_problem)


<center>
**wykład 2**
</center>

- nieco mniej chaotyczne [slajdy](---ThisDir---/ms_2.pdf)
- nowe, króciutkie, [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EX1qBOu3wMZMsWNJ-P-RwGsBAachwZlIjVar_SU-cAlSEQ)
  - postanowiłem sporządzić od zera nowe nagranie do "mniej chaotycznych" slajdów
  - jest bardzo krótkie, pomijam wiele obliczeń - proszę je jednak dokładnie prześledzić
- notebooki Mathematici
  - wystarczy uruchomić w mathematice pliki *.nb* i w menu *Evaluation - Evaluate All*
  - instrukcja instalowania Mathematici dla studentów zajduje się w tekście [strony](https://kacpertopol.github.io/000pl.html), 
	  proszę uważnie przeczytać tekst jak również PDF, który jest do ściągnięcia z tej strony	
  - [notebook](---ThisDir---/examples.nb) rozkład normalny 2D
	  - proszę czytać komentarze
  - [notebook](---ThisDir---/examples1.nb) macierz kowariancji oraz zamiana zmiennych w 2D
	  - proszę czytać komentarze
- [anieta](https://forms.office.com/r/GauqxyJPFU)
- YouTube
  - jest mnóstwo materiałów, proszę sobie wpisać hasła takie jak "Jacobian", "change of variables"

<center>
**wykład 3**
</center>

- [slajdy](---ThisDir---/wyklad_3.pdf)
- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/EdR3X9a13fxNhbFXGGwTI9sBFe_yGXrUM5M15T8yQN8dRg?e=dHChaG)
- [notebook Mathematici](---ThisDir---/05_12_2020.nb)
  - po uruchomieniu w Mathematice wystarczy *Evaluation -> Evaluate Notebook*
- krążyłem wokół tego tematu podczas wykładu ale chyba w końcu nie podałem definicji - czy po wykonaniu ćwiczeń
  potrafią Państwo powiedzieć czym jest stan stacjonarny?

<!---
<center>
**wykład 4**
</center>

<center>
(20 XII 2020)
</center>

- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/ERUnK5HhpQRJm6vAz1wvIOMB-dV6CH8OmZU7TyFEcU40iQ?e=I2YRqC) 
- [slajdy](---ThisDir---/20_12_2020.pdf)
- wykład korzystał również z:
  - [rodzaje łańcuchów](http://wwwf.imperial.ac.uk/~ejm/M3S4/NOTES3.pdf)
  - [unikalność rozwiązania](http://www.stat.yale.edu/~jtc5/251/readings/Basics%20of%20Applied%20Stochastic%20Processes_Serfozo.pdf) 
  - [dodatkowy wykład 1](https://mast.queensu.ca/~stat455/lecturenotes/set3.pdf)
  - [dodatkowy wykład 2](https://siamak.isoperimetric.info/teaching/markov/files/equilibrium-2.pdf)
  - [dodatkowy wykład 3](http://math.uchicago.edu/~may/REU2017/REUPapers/Freedman.pdf)
- notebooki Mathematici 
  - [Bernulli](---ThisDir---/20_12_2020.nb)
  - [Markov](---ThisDir---/20_12_2020_1.nb)
  - TODO: Metoda Funkcji Generującej

<center>
**wykład 5**
</center>

<center>
(10 I 2021)
</center>

- [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/ESgo0-PppftKt6oLnx4561YBeWm8hRXuTRHnwoLyscFX6w?e=jCgjar)
- [slajdy](---ThisDir---/wyklad_5.pdf)
- [notebook](---ThisDir---/autocorrelation.nb) Mathematici 
  - wystarczy uruchomić notebook (Evaluate Notebook)
  - TODO - pojawi się uzupełniona wersja z wartościami oczekiwanymi dla procesu liczącego Bernulliego

<center>
**wykład 6**
</center>

<center>
(23 I 2021)
</center>

- [slajdy](---ThisDir---/W6.pdf)
- [notebook](---ThisDir---/infiniteMatrix.nb)
  - wystarczy uruchomić notebook (Evaluate Notebook)
  - na samym dole jest `Manipulate` z przykładem omawianym na wykładzie

--->
