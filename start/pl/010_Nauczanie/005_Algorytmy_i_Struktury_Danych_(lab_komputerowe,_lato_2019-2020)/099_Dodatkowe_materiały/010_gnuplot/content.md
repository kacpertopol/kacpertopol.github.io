* [Główna strona](http://www.gnuplot.info/) programu gnuplot.

* [Przykładowy skrypt](---ThisDir---/przyklad_gnuplot) programu `gnuplot` zawierający dane do narysowania wykresu
  * Aby uruchomić skrypt wystarczy nadać mu uprawnienia do wykonywania:
    
    `$ chmod +x przyklad_gnuplot`
	  
    oraz wykonać:

    `$ ./przyklad_gnuplot`

* [Przykładowy program](---ThisDir---/przyklad1_gnuplot) napisany w języku programu gnuplot oraz [dane](---ThisDir---/dane) do wykresu.
  * Aby uruchomić program wystarczy w katalogu zawierającym dane oraz program wykonać:
	  
    `$ gnuplot przyklad1_gnuplot`

  * Zalecam tworzenie skryptów tak jak w pierwszym podpunkcie. Dzieki temu dane oraz instrukcje 
	  potrzebne do ich narysowania trzymane są w jednym miejscu. 
* [Jeszcze jeden przykład](---ThisDir---/przyklad2_gnuplot), tym razem wykres jest zapisywany do pliku `example.pdf`.
  * Aby uruchomić program wystarczy w katalogu zawierającym dane oraz program wykonać:
	  
    `$ gnuplot przyklad2_gnuplot`
  * Dane są wczytywane z pliku [dane](---ThisDir---/dane)
