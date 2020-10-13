---
title : Zestawy zadań
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Old_Fashioned_Gym_%287981005513%29.jpg/800px-Old_Fashioned_Gym_%287981005513%29.jpg)](https://commons.wikimedia.org/wiki/File:Old_Fashioned_Gym_(7981005513).jpg)
</center>





# Zawartość:

* [Ocenianie](#ocenianie)
* [Zestaw 1 (8 X 2020)](#zestaw-1-8-x-2020)



# Ocenianie

- Ćwiczenia można oddawać na każdych zajęciach,
  wystarczy zademonstrować działanie programu oraz króciutko
	o nim opowiedzieć.
- Ćwiczenia z zestawu przypadającego na dane zajęcia
  można oddawać na tych zajęciach lub dwóch kolejnych.
- Ocena z zadań będzie
  wystawiana na podstawie całkowitej ilości
  punktów uzyskanych z rozwiązania ćwiczeń. 




# Zestaw 1 (8 X 2020)

<center>
**MATERIAŁY DODATKOWE**
</center>

Tworzenie skryptu, metoda 1 (prostsza):

- po uruchomieniu programu mathematica należy w menu wybrać:
  *File - New - Package/Script - Wolfram Language Script*
- w nowym okienku mozna wpisać treść programu
- po zakończeniu edycji zapisujemy skrypt i zamykamy okienko 
  (to ważne, Mathematica
  korzysta z mechanizmu uniemożliwiającego jednoczesną edycję
  oraz wykonanie skryptu)
- w terminalu (pod linuxem [tak](https://help.ubuntu.com/community/UsingTheTerminal), pod windows [tak](https://www.wikihow.com/Open-Terminal-in-Windows)) nawigujemy do katalogu gdzie znajduje się skrypt
  i uruchamiamy komendą (pod linux, pod windows jest trochę inaczej - proszę samodzielnie po eksperymentować):
	
  ```bash
	... $ ./nazwa_skryptu.wls
	```

Tworzenie skryptu, metoda 2 (linux ale bardziej uniwersalna w tym systemie):

- otwieramy ulubiony edytor tekstu
- wpisujemy do pliku program
- w pierwszej linijce (tzw linijka "hash bang!", musi być zawsze pierwsza, nad nią nie mogą się znajdować puste linie) dodatkowo dodajemy:
  
  ```bash
  #!/usr/bin/env wolframscript
  ```

- linijka ta informuje system operacyjny, który program 
  powinien być wykorzystany do zinterpretowaniu programu 
  zawartego w skrypcie

- alternatywnie można zamieścić bezpośrednią ścieżkę do programu,
  na moim systemie wygląda ona następująco:

  ```bash
  #!/usr/local/Wolfram/Mathematica/12.1/Executables/wolframscript
  ```

- teraz wystarczy nawigować w terminalu do katalogu zawierającego skrypt, zezwolilć aby nasz skrypt był wykonany:

  ```bash
	... $ chmod +x nazwa_skryptu
	```

- ... i go wykonać:

  ```bash
	... $ ./nazwa_skryptu
	```

- skrype można również wykonać z argumentami, np:

  ```bash
	... $ ./silnia 5
	```

Kilka przykładowych skryptów:

- [Hello world!](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/hello.wls)
- [silnia](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/silnia)

Kilka chaotycznych notebooków z zajęć (polecam zaglądnąć najpierw do materiałów profesora Jacka Golaka):

- [pierwszy bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/nof_08_10_2020_A.nb) 
- [drugi bałagan](./start/pl/010_Nauczanie/007_Narzędzia_Obliczeniowe_Fizyki_(lab_komputerowe,_zima_2020-2021)/010_Zestawy_zadań/001_Zestaw_1_(8_X_2020)/nof_08_10_2020_B.nb)

<center>
**A**
</center>

<center>
(1 punkt)
</center>

Proszę zainstalować i uruchomić program *Mathematica*.

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Korzystająć z *notebook*a proszę zaimplementować ciąg
liczb Fibonacciego $0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21, \ldots$.

<center>
**C**
</center>

<center>
(2 punkty)
</center>

Korzystając z implementacji z zadania **B** proszę stworzyć
uruchamialny skrypt. Skrypt powinien z linii poleceń pobierać pojedyńczy argument, 
liczbe wyrazów w ciągu Fibonacciego. Państwa program powinien następnie wypisywać na ekranie
odpowiednią liczbę początkowych wyrazów tego ciągu.


