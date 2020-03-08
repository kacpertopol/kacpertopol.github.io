<center>
**A** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(1 punkt)
</center>

Implementacja zbioru wykorzystująca jednowymiarowe tablice
o skończonym rozmiarze z zadania **A** w zestawie 1 zakłada,
że każdemu elementowi zbioru można przypisać liczbę naturalną
$1 \ldots N$. Proszę zaimplementować funkcje implementujące
takie przyporządkowanie dla zbiorów:

* liczb całkowitych $n , n + 1 , n + 2 , \ldots , m$ gdzie $n < m$
* liczb całkowitych $n , n + 2 , n + 4 , \ldots , m$ gdzie $n < m$
* liter $a , b , c , \ldots , z$, bez polskich znaków ęóąśłżźć 
* dwuliterowych napisów, gdzie każda litera jest z zakresu $a - z$ bez polskich znaków ęóąśłżźć

<center>
**B** 
</center>

<center>
[[źródło](https://onlinelibrary.wiley.com/doi/abs/10.1002/bimj.4710260406)]
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować typ danych `setHashed` reprezentujący
matematyczny zbiór oraz operacje
które dla dwóch zbiorów $A$, $B$ realizują:

* sumę zbiorów $A \cup B$
* część wspólną zbiorów $A \cap B$
* różnicę zbiorów $A - B$
* sprawdzanie identyczności zbiorów $A \equiv B$

oraz dla elementu $x$ i zbioru $A$ realizują:

* wstawianie $x$ do zbioru $A$
* usuwanie $x$ ze zbioru $A$
* sprawdzanie czy $x \in A$

Tym razem proszę wykrzystać haszowanie otwarte.
Państwa implementację proszę wykorzystać w programie, który bada
złożoność obliczeniową poszczególnych operacji.
Dla każdej z zaimplementowanych operacji program powinien produkować jeden plik,
który może być uruchomiony z wykorzystaniem programu [gnuplot](http://www.gnuplot.info/). 
W wiadomości e-mail proszę
opisać podejście wykorzystane do badania złożoności obliczeniowej
i skonfrontować Państwa wyniki z wartościami teoretycznymi.

<center>
**C** 
</center>

<center>
(1 punkt)
</center>

Korzystając z wyników zadań **A** oraz **B** z zestawu 1
oraz zadania **B** z obecnego zestawu proszę się zastanowić która implementacja
jest lepsza i w jakiej sytuacji. Swoją odpowiedź (popartą odpowiednimi wykresami) proszę przesłać za pośrednictwem e-mail.

Aby ułatwić Państwu zadanie, proszę założyć, że elementami przechowywanymi
we wszystkich zbiorach są słowa składające się z 4 liter (bez polskich znaków).
Można wykorzystać zadanie **A**.

<center>
**UWAGI**
</center>

* Dla każdej implementacji typu danych oraz dla każdej zaimplementowanej operacji proszę dodatkowo:
  * zamieścić w Państwa programie test sprawdzający czy operacje są zaimplementowane prawidłowo
  * aby ułatwic Państwu pracę możemy się umówić, że w teście będzie sprawdzana niewielka ilość
	  przypadków - na tyle mała aby można było je wypisać na ekranie komputera i przeanalizować
* Badając złożoność obliczeniową operacji, proszę się zastanowić jak powina
  wyglądać zależność $t(n)$ czasu wykonania problemu ($t$) od rozmiaru 
	problemu ($n$)
	i nanieść tą hipotezę na odpowiedni wykres.
* Sprawdzenie złożoności obliczeniowej dla każdej z operacji może być trochę pracochłonne.
  Kryteria zaliczenia zadań są złagodzone: wystarczy jeden wykres dla wybranej operacji.
  Ale proszę go jednak zrobić porządnie :-)
* Kilka wykresów dla zadania **B** z różną liczbą "klas" albo "porcji" na które może wskazywać funkcja haszująca:
  [1](---ThisDir---/sh1.pdf), [2](---ThisDir---/sh2.pdf), [3](---ThisDir---/sh3.pdf), [4](---ThisDir---/sh4.pdf), 
  [5](---ThisDir---/sh5.pdf), [6](---ThisDir---/sh6.pdf), [7](---ThisDir---/sh7.pdf), [8](---ThisDir---/sh8.pdf), 
  [9](---ThisDir---/sh9.pdf), [10](---ThisDir---/sh10.pdf), ..., [100](---ThisDir---/sh100.pdf) 
* W większości zadań nie jest określony typ danych elementów zbioru. Można korzystać na przykład z liczb całkowitych. 
  Nie powinno mieć to większego znaczenia
  jeżeli pewne warunki są spełnione. Jakie to warunki?
    * Wskazówka: $\equiv$, $\lt$, $\gt$

