Porozmawiamy o zadaniach programistycznych
prof. Pawła Góry, dostępnych [tutaj](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/numeryczne.pdf).
Będę prosił Państwa o wykonanie części tych zadań.
Proszę nie panikować 😉 , kryteria oceniania będą łagorniejsze niż opisane w tym dokumencie.

<center>
**MATERIAŁY DODATKOWE**
</center>

- [standard IEE 754](https://en.wikipedia.org/wiki/IEEE_754) 
- [postać Hornera](https://en.wikipedia.org/wiki/Horner%27s_method)

<center>
**A**
</center>

<center>
(1 punkt)
</center>

Korzystając z ulubionego języka (w przypadku egzotycznych języków proszę o skonsultowanie) 
proszę napisać program, który będzie testował reprezentacje liczb zmiennoprzecinkowych.
Proszę w programie zbadać

- granice reprezentacji "single precision" 
- granice reprezentacji "double precision" 

Eksperyment powinien:

- demonstrować co się dzieje w przpadku gdy pojawia się liczba przekraczająca zakres reprezentacji
  - liczba może być zarówno zbyt mała jak i zbyt duża
- pokazać jak można bezpiecznie obsłużyć sytuacje w których pojawiają się liczby zmiennoprzecinkowe
  przekraczające granice reprezentacji

<center>
**B**
</center>

<center>
(2 punkt)
</center>

Korzystając z ulubionego języka (z zastrzeżeniem jak wyżej) proszę zaimplementować następujący pseudokod:

```
function iteruj(mianownik)
	dx = 1.0 / float(m)
	x = 0.0
	do i = 1 .. mianownik
    	x = x + dx
    end do
    return abs(1.0 - x)
```

Gdzie `mianownik` to dodatnia liczba całkowita, `1.0` oraz `0.0` to liczby zmiennoprzecinkowe,
funkcja `float` zamienia liczbę całkowitą na liczbę zmiennoprzecinkową natomiast funkcja `abs`
zwraca wartość bezwzględną.

Korzystając z implementacji:

- proszę zbadać jak zmieni się wynik funkcji gdy `mianownik = 1 .. 2048`
- proszę zbadać jak zmieni się wynik funkcji gdy:
  - liczby zmiennoprzecinkowe reprezentowane są w pojedynczej precyzji
  - liczby zmiennoprzecinkowe reprezentowane są w podwójnej precyzji
- otrzymane wyniki proszę zinterpretować i skomentować :-) 

<center>
**C**
</center>

<center>
(2 punkt)
</center>

Proszę (ulubiony język, etc) zaimplementować przykład z wykładu profesora. Mamy zatem ciąg:

$$
\left\{
	\begin{array}{ll}
		x_{n + 1} = 4 x_n - 1 \\
		x_{0} = \frac{1}{3}
	\end{array}
\right.
$$

i badamy jego rozbieżność. Proszę w implementacji wykorzystać
szeroki wachlarz reprezentacji liczb zmiennoprzecinkowych.
Wyniki proszę zilustrować wykresem. 

<center>
**D**
</center>

<center>
(3 punkt)
</center>

Będziemy szukać miejsc zerowych wielomianu:

$$
x^{2} - 4 x + (4 + \alpha) = 0
$$

gdzie $\alpha$ jest niewielkim zaburzeniem, którego
wartość jest porównywalna z precyzją maszynową
odpowiedniej reprezentacji liczb zmiennoprzecinkowych.

Proszę zbadać jak czułe są wyliczone numerycznie miejsca
zerowe tego wielomianu na drobne (rzędy precyzji maszynowej)
zmiany $\alpha$. Dodatkowo rozwiązanie powinno:

- być zilustrowane wykresem
- zinterpretowane
- wykonane dla różnych reprezentacji liczb zmiennoprzecinkowych (pojedyncza, podwójna precyzja)

<center>
**E**
</center>

<center>
(3 punkt)
</center>

Mamy dwa wielomiany:

$$
p(x) = x^5-\frac{137 x^4}{60}+\frac{15 x^3}{8}-\frac{17 x^2}{24}+\frac{9 x}{8}-\frac{1}{120}
$$

oraz

$$
q(x) = x \left(x \left(x \left(\left(x-\frac{137}{60}\right) x+\frac{15}{8}\right)-\frac{17}{24}\right)+\frac{9}{8}\right)-\frac{1}{120}
$$

Można sprawdzić, że $p = q$ (warto zajrzeć do **MATERIAŁY DODATKOWE** o postaci Hornera). Proszę, zaimplementować
iteracje:

$$
\left\{
	\begin{array}{ll}
		x_{n + 1} = p(x_{n}) \\
		x_{0} = \frac{2}{3}  \\
		y_{n + 1} = q(y_{n}) \\
		y_{0} = \frac{2}{3}
	\end{array}
\right.
$$

następnie:

- porównać wartości $x$ oraz $y$ w kolejnych iteracjach
- sprawdzić czy dominującym źródłem różnic jest:
  - inna kolejność wykonywania mnożenia i dodawania
  - reprezentacja numeryczna liczb zmiennoprzecinkowych

Uwaga, implementując obydwie postacie wielomianu należy pamiętać o kolejności wykonywania
operacji.


