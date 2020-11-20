<center>
**RÓWNANIE FALOWE Z PERIODYCZNYMI WARUNKAMI BRZEGOWYMI**
</center>

<center>
*projekt oczekuje na dwie realizujące osoby*
</center>

Proszę przyjrzeć się zadaniu **E** z zestawu $5$ (05 XI 2020). Korzystając z macierzy
podobnej do zdefiniowanej w tym zadaniu proszę rozwiązać równanie falowe z periodycznymi
warunkami brzegowymi w dwóch wymiarach. Można sobie wyobrazić, że fala rozchodzi się 
na kwadratowej płycie o długości boku $L$. Periodyczność warunków brzegowych polega na tym,
że "sklejamy" lewą oraz prawą krawędź płyty oraz górną i dolną krawędź. Powstaje obiekt
przypominający powierzchnię torusa. 
Proszę założyć, że fala rozchodzi się z prędkością
$v$. Pakiet powinien implementować następujące funkcje:

- zmiana warunków początkowych (wstępnego rozkładu naprężeń w drucie)
- zmiana prędkości rozchodzenia się fali
- zmiana długości boku $L$
- wizualizacja ewolucji czasowej fali w trzech wymiarach na powierzchni torusa

Ciekawostka. Fale rozchodzące się w strunie były wykorzystywane w pamięci RAM:

<!--BEGIN_HTML
<div>
  <div style="position:relative;padding-top:28.13%;">
	<iframe 
	   style="position:absolute;top:0;left:25%;width:50%;height:100%;" 
	   src="https://www.youtube.com/embed/2BIx2x-Q2fE" 
	   frameborder="0" 
	   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	   allowfullscreen>
	</iframe>
  </div>
</div>
END_HTML-->

<br/><br/>

<center>
**SYMULACJA UKŁADÓW OPTYCZNYCH**
</center>

<center>
*G. Ż. oraz M. J.*
</center>

Symulacja uładów optycznych w dwóch wymiarach.
Pakiet powinien implementować następujące funkcje:

- ustawiania własności optycznych środowiska
- dodawanie soczewki
  - użytkownik podaje pozycję, ogniskowa i materiał
  - soczewka powinna mieć określony kształt i rozmiar 
  - nie wystarczy posłużyc się wyidealizowanym modelem "nieskończenie" cieńkiej soczewki
- dodawanie lustra
  - lustra sferyczne oraz paraboliczne
- wizualizacja układu optycznego
- wizualizacja promieni oraz snopów promieni
  - powinna być możliwość okreslenia koloru promieni
  - załamanie promienia w kontakcie z powierzchnią soczewki powinno zależeć od 
    koloru (długości fali światła) promienia

Projekt jest dość złożony dlatego zakładam, że jego realizacją zajmą się dwie osoby.
Byłoby fantastycznie gdyby udało się Państwu zademonstrować aberracje:

<!--BEGIN_HTML
<div>
  <div style="position:relative;padding-top:28.13%;">
	<iframe 
	   style="position:absolute;top:0;left:25%;width:50%;height:100%;" 
	   src="https://www.youtube.com/embed/EL9J3Km6wxI" 
	   frameborder="0" 
	   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	   allowfullscreen>
	</iframe>
  </div>
</div>
END_HTML-->

<br/><br/>

<center>
**POTENCJAŁ ORAZ POLE ELEKTRYCZNE W DWÓCH WYMIARACH**
</center>

<center>
*projekt oczekuje na dwie realizujące osoby*
</center>

Rachunek potencjału oraz pola elektrycznego w systemie
ze statecznymi ładunkami elektrycznymi. Pakiet powinien 
implementować następujace funkcje:

- dodawanie elektrod o dowolnych kształtach oraz potencjałach:
  - kół
  - elips
  - poligonów
- wizualizacja linii pola
- wizualizacja powierchni ekwipotencjalnych

W rozwiązaniu można założyć, że po prawej stronie równania Poissona jest 
wszędzie, oprócz miejsc zajmowanych przez elektrody, $0$. Następnie
można podzielić płaszczyznę z elektrodami kwadratową siatką i skorzystać
z [metody Gaussa - Seidela](https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method).

<!--BEGIN_HTML
<div>
  <div style="position:relative;padding-top:28.13%;">
	<iframe 
	   style="position:absolute;top:0;left:25%;width:50%;height:100%;" 
	   src="https://www.youtube.com/embed/QpVxj3XrLgk"
	   frameborder="0" 
	   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	   allowfullscreen>
	</iframe>
  </div>
</div>
END_HTML-->

<br/><br/>

<center>
**NAPRĘŻENIA W MAKARONOWYM MOŚCIE**
</center>

<center>
*projekt oczekuje na dwie realizujące osoby*
</center>

Rachunek naprężeń w dwu wymiarowym moście skonstruowanym z makaronu spaghetti.
Pakiet powinien implementować następujące funkcje:

- dodawanie punktów łączących kilka suchych nitek makaronu
- dodawanie suchych nitek makaronu pomiędzy punktami łączącymi
- określanie, które punkty łączące są podporami
- określanie, które punkty łączące są obciążone
- wizualizacja mostu
- rachunek naprężeń mostu zakładająć, że punkty łączące nie zmienią położenia
- wizualizacja naprężeń w moście

<!--BEGIN_HTML
<div>
  <div style="position:relative;padding-top:28.13%;">
	<iframe 
	   style="position:absolute;top:0;left:25%;width:50%;height:100%;" 
	   src="https://www.youtube.com/embed/y1z66EC4n4o"
	   frameborder="0" 
	   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	   allowfullscreen>
	</iframe>
  </div>
</div>
END_HTML-->


<br/><br/>



