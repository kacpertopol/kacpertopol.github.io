<center>
**NOTEBOOK NA START Z PROJEKTAMI**
</center>

- [notebook](---ThisDir---/start.nb) zawiera fragmenty implementacji, które mogą się przydać na start 
  - po otwarciu wystarczy `Evaluate Notebook`
  - podzielony na części odpowiadające projektom

<center>
**RÓWNANIE FALOWE Z PERIODYCZNYMI WARUNKAMI BRZEGOWYMI**
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

Rachunek naprężeń w dwu wymiarowym moście skonstruowanym z makaronu spaghetti.
Pakiet powinien implementować następujące funkcje:

- dodawanie punktów łączących kilka suchych nitek makaronu
- dodawanie suchych nitek makaronu pomiędzy punktami łączącymi
- określanie, które punkty łączące są podporami
- określanie, które punkty łączące są obciążone
- wizualizacja mostu
- rachunek naprężeń mostu zakładając, że punkty łączące nie zmienią położenia
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

<center>
**LICZENIE PI**
</center>

Proszę uważnie obejrzeć film jak również części 2 oraz 3 z opisu na *Youtube*.
Projekt polega za zaimplementowaniu takiej symulacji. Pakiet powinien
implementować:

- wybór masy obydwu klocków
- wizualizację ewolucji czasowej klocków
- tworzeniu "dźwięku" wydawanego podczas zderzeń

<!--BEGIN_HTML
<div>
  <div style="position:relative;padding-top:28.13%;">
	<iframe 
	   style="position:absolute;top:0;left:25%;width:50%;height:100%;" 
	   src="https://www.youtube.com/embed/jsYwFizhncE"
	   frameborder="0" 
	   allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
	   allowfullscreen>
	</iframe>
  </div>
</div>
END_HTML-->

<center>
**SYMULACJA UKŁADÓW PLANETARNYCH**
</center>

Pakiet powinien implementować symulację ewolucji czasowej kilku ciał oddziaływujących grawitacyjnie.
Powiniej zawierać następujące funkcje:

- dodawanie ciał o zadanej pozycji, prędkości początkowej oraz masie
- wizualizację ewolucji czasowej systemu

Doskonale by było gdyby udało się:

- zrobić symulację układu słonecznego
- zademonstrować chaos w układach z trzema lub więcej ciałami

