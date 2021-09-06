---
title : Symulacje w czasie rzeczywistym
---

<center>
[![](https://upload.wikimedia.org/wikipedia/commons/6/62/Pong_Game_Test2.gif)](https://commons.wikimedia.org/wiki/File:Pong_Game_Test2.gif)
</center>



# Zawartość:

* [Organizacja](#organizacja)
* [Zestawy zadań](./00pl_inv.html)



# Organizacja

Zajęcia będa się odbywać z wykorzystaniem ZOOM. Poniżej znajdują się dane potrzebne do dołączenia
do zajeć:

- link: <https://us02web.zoom.us/j/84466952075?pwd=UFMzMThBd1liK3VBVXlLU0NnYWltdz09>
- Meeting ID: `844 6695 2075`
- Passcode: `t63i53`

Zajęcia będą podzielone na dwie części. W pierszej będę tłumaczył nowe zadania, natomiast druga część
przeznaczona jest na indywidualne konsultacje i oddawanie zadań.
Ocena z ćwiczeń będzie wystawiona na podstawie liczby wykonanych zadań (50%) oraz projektu końcowego (50%). 
Aby zaliczyć zadanie należy:

- przesłać spakowane pliki na <kacper.topolnicki@uj.edu.pl>, w temacie wiadomości powinien znaleźć się ciąg znaków "SYMULACJE20202021"
- połączyć się ze mną na ZOOM, udostepnić ekran, zademonstrować rozwiązanie i opowiedzieć o swojej implementacji

Aby zaliczyć 
ćwiczenia trzeba mieć pozytywną ocenę z zadań i projektu.

Propozycje projektów (można zgłaszać również swoje propozycje):

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

Pytania na egzamin (lista będzie aktualizowana) [źródło: wykłady do przedmiotu "Programowanie symulacji fizyki w czasie rzeczywistym"]:

1. (wykład 1) Omów znaczenie programowania fizyki w kontekście
  tworzenia gier wideo. Wskaż różnice pomiędzy programowaniem
  symulacji fizyki w czasie rzeczywistym (real-time) oraz symulacjami
  autonomicznymi (off-line). Silniki fizyki. Wsparcie obliczeń poprzez
  **ppu** i **gpgpu**. Wymień układy fizyczne, które są
  najczęściej obsługiwane przez silniki fizyki czasu rzeczywistego. 
2. (wykład 2) Przedstaw ogólnie metodykę opisywania ruchu układu
  fizycznego (stopnie swobody, zmienne stanu, wektor stanu, równanie
  ewolucji). Opisz ogólnie dyskretyzację równania ewolucji oraz główne
  zadanie silnika fizyki.
3. (wykład 2) Omów problem synchronizacji silnika fizyki z pętlą
  główną gry. Wyjaśnij, czym różnią się algorytmy fizyki ze stałym
  krokiem czaso- wym od algorytmów z adaptywnym krokiem czasowym. 
4. (wykład 3) Omów zagadnienie stabilności algorytmów. Opisz wpływ na
  stabil- ność takich rzeczy jak jawność/niejawność algorytmów, użycie
  pochod- nych progresywnych/wstecznych, użycie tłumienia.
5. (wykład 3) Przedstaw metodykę numerycznego rozwiązywania równań
  dyna- miki punktu materialnego. Podaj przykład struktury danych
  reprezen- tującej punkt materialny. Omów algorytm Eulera.
6. (wykład 3) Wskaż najważniejsze cechy algorytmów numerycznego
  rozwiązy- wania równań różniczkowych w rzeczywistym czasie.
7. Omów algorytm Verleta i jego modyfikacje. Przedstaw, jak
  różnice centralne i średnie centralne poprawiają dokładność
  obliczeń.
8. (wykład 4) Podaj podstawowe algorytmy numerycznego całkowania
  równań różniczkowych zwyczajnych. Wyjaśnij różnicę pomiędzy
  schematami jawnymi i niejawnymi.
9. (wykład 4) Wyjaśnij różnicę pomiędzy metodami całkowania równań
  różniczkowych ze stałym i adaptywnym krokiem czasowym. Omów predykcje
  akumulacji błędu oparte o błąd maksymalny lub błądzenie losowe.
10. (wykład 4) Omów modelowanie układów punktów materialnych (modele
  cząsteczkowe). Podaj postać funkcji stanu i równania ewolucji. Wskaż
  na różnicę między bezstanowymi i zapamiętującymi stan modelami
  cząsteczkowymi.
11. (wykład 5) Wyjaśnij różnicę między algorytmami dyskretnymi
  (a posteriori) i ciągłymi (a priori) obsługi kolizji. Podaj
  przykłady algorytmów.
12. (wykład 5)  Omów podział algorytmu detekcji kolizji na fazy
  detekcji kolizji i odpowiedzi kolizji. Uzasadnij znaczenie
  algorytmów optymalizujących detekcję zderzeń obiektów. Podaj
  przykłady takich algorytmów.
13. (wykład 5) Opisz modelowanie zderzeń punktów materialnych
  z nieruchomymi obiektami (detekcja kolizji, geometria zderzenia,
  fizyka zderzenia, odpowiedź kolizji).
14. (wykład 5) Omów algorytm Eulera dla punktów materialnych wraz
  z dyskret nym algorytmem obsługi kolizji punktów z płaszczyzną.
19. (wykład 6) Przedstaw model masy na sprężynce. Wyjaśnij, dlaczego
  sprężynę można traktować jako nieważką. Opisz różne przypadki
  tłumienia drgań. Omów dowolny algorytm numeryczny wyznaczania ruchu.
20. (wykład 6) Omów modele układów mas i sprężynek (ang.
  *mass-spring systems*). Zdefiniuj siły wewnętrzne
  (sprężystości, sztywności, tłumienia drgań), zewnętrzne
  i kontaktowe. Podaj przykłady zastosowań modelowania z zastosowaniem
  układów elastycznych.
21. (wykład 6) Omów podstawowe zalety i wady modeli układów mas
  i sprężynek (ang. *mass-spring systems*). Przedstaw koncepcje
  najpopularniejszych optymalizacji (metody z dłuższymi krokami
  czasowymi, szybkie symulacje).
24. (wykład 7) Podaj definicję bryły sztywnej i liczbę stopni swobody.
  Omów mo- del dyskretny i model ciągły. Zdefiniuj współrzędne
  offsetowe pun- któw bryły sztywnej. Podaj interpretację kierunku,
  zwrotu i wartości wektora prędkości kątowej. Podaj definicję
  macierzy tensora momentu bezwładności. Podaj wzór na całkowity
  moment pędu bryły sztywnej.
25. (wykład 7) Wypisz równania Newtona-Eulera ruchu bryły sztywnej.
  Wyjaśnij, dlaczego nie nadają się na równania ewolucji, które są
  bezpośrednio rozwiązywane numerycznie w czasie rzeczywistym.
26. (wykład 7) Opisz reprezentację struktury danych dla bryły sztywnej
  z użyciem macierzy obrotu. Podaj pełne równania ewolucji.
27. (wykład 8) Opisz reprezentację struktury danych dla bryły sztywnej
  z użyciem kwaternionów. Podaj pełne równania ewolucji.
28. (wykład 8) Opisz reprezentację struktury danych dla bryły sztywnej
  z użyciem kątów Eulera. Podaj pełne równania ewolucji.
29. (wykład 8) Porównaj wady i zalety trzech podstawowych sposobów
  reprezen- tacji ruchu obrotowego bryły sztywnej (kąty Eulera,
  macierz obrotu, kwaterniony).
30. (wykład 9) Omów etap ogólny (ang. *broad phase*) oraz etap
  szczegółowy (ang. *narrow phase*) algorytmu obsługi detekcji
  kolizji.
31. (wykład 9) Podaj i omów twierdzenie **sat** (ang.
  *separating axis theorem*). Podaj definicję funkcji nośnika
  (ang. *support function*) i odwzorowania nośni- ka
  (ang. *support mapping*). Przedstaw twierdzenie **sat**
  sformułowane z użyciem funkcji nośnika.
32. (wykład 9) Omów wersję twierdzenia **sat** dla wielościanów
  wypukłych. Podaj, jak tworzyć zbiór kierunków kandydatów na osie
  separacji (**sac**).



# [Zestawy zadań](./00pl_inv.html)


