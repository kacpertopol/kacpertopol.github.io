<center>
**LITERATURA**
</center>

Podręczniki:

- [*Probability, Random Processes, and Statistical Analysis* Hisashi Kobayashi, Brian L. Mark, William Turin](https://www.cambridge.org/core/books/probability-random-processes-and-statistical-analysis/1909C657E4758038B54C4235B3AD0FDF)
- [*Probability and Statistics for Computer Scientists* Michael Baron](https://www.routledge.com/Probability-and-Statistics-for-Computer-Scientists/Baron/p/book/9781138044487)
- [*Probability Theory: The Logic of Science*  E. T. Jaynes (Author), G. Larry Bretthorst (Editor)](https://www.amazon.com/Probability-Theory-Science-T-Jaynes/dp/0521592712)
  - są równiez dostępne  [nagrania](https://youtube.com/playlist?list=PL9v9IXDsJkktefQzX39wC2YG07vw7DsQ_&si=SYkFZQd4WvUxzdRC) wykładów powiązane z tą książką

Popularne:

- [*Thinking, Fast and Slow* Daniel Kahneman](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)
- [*Bernoulies Fallacy* Aubrey Clayton](https://www.amazon.com/Bernoullis-Fallacy-Statistical-Illogic-Science/dp/0231199945)

<center>
**MATERIAŁY DODATKOWE**
</center>

- [Instrukcją instalacji](https://fais.uj.edu.pl/documents/41628/5097967/Oprogramowanie+Mathematica_na_Uniwersytecie_Jagiello%C5%84skim_WFAIS.pdf/e644e1f3-74bb-408e-9f64-529bc329d1e7) programu Mathematica (aka WolframNB).
  - **UWAGA** wszędzie gdzie to konieczne należy wpisywać uniwersytecki adres e-mail. Licencją objęty jest uniwersytet a e-mail stanowi metodę weryfikacji, że jesteście państwo studentami uczelni. Informacja o aktywacji studenckich kont pocztowych dostępna jest [tutaj](https://pomocit.uj.edu.pl/poczta_studenci) 
    w zakładce “Aktywacja kont pocztowych dla studentów i doktorantów”.

<center>
**BŁĘDY, UWAGI, SUGESTIE**
</center>

Błędy, sugestie, uwagi proszę zgłaszać na adres email [kacper.topolnicki@uj.edu.pl](mailto:kacper.topolnicki@uj.edu.pl). 
Dziękuję!

<center>
**wykład 1**
</center>

1. Aksjomaty Kolmogorova, prawdopodobieństwo subiektywne:
    a) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQBk59HfZeF3RYKzVcpog_KjAcIQBhNDc8epJ7fkeEV_qCY?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=vj4pBn), [notatki](---ThisDir---/kolmogorow.pdf)
2. Prawo Bayesa, problem urny:
    a) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQDyElUwQeTRTpJK6u-aAJvoAeZ7K0owWjgeDmtfjPxH1jE?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=rOfmvl), [notatki](---ThisDir---/urn_theory.pdf)
    b) praktyczna implementacja w języku [Julia](https://julialang.org/): [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQBgZwii3oVdRZRVsg1uNo0lATMlbf60ZurjmYU7fIuz0LE?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=nIu4cg), [program](---ThisDir---/urn_julia.jl)
3. Problem Montiego Halla:
    a) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQCZou8vwzh2RJywR45QlsiJAU8GWTNF6siOLR_Ek2YbnZ8?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=FQ1V1v), [notatki](---ThisDir---/monty_hall_theory.pdf)
    b) praktyczna implementacja w języku python: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQDtE63bpss2T4P2AAcQ0i3wATBGis7Jpgk7KGGJG_ytc6w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=03pgzR), [program](---ThisDir---/monty_hall_python.py)
4. Zmienne losowe:
    a) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQCVEBjqmCeQS6xWw0xU2P97AYfcJymleNbOK-N5otw0Lbg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=oAtfQH), [notatki](---ThisDir---/zmienne_losowe.pdf)
5. Centralne twierdzenie graniczne, rozkład normalny, rozkład Cauchiego:
    a) praktyczny przykład w Wolfram Language: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQDA8nomQpu0SLQ-xYRi1fayAVr3W0FsnlIjuSJ8VRM948g?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=3JRoNM), [notebook](---ThisDir---/central_limit_theorem_wolfram_language.nb)
    b) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQAYgz-MVuwaS4sebt3IaFUCAQ8RrVh2xmGLTQWvej7Yx7k?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=3xFIUC), [notatki](---ThisDir---/central_limit_theorem_theory.pdf)
6. Zmiana zmiennych losowych:
    a) praktyczny przykład w Wolfram Language: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQC9k9XLRellTpr0usAwPE1SAUly3TNAJ9K2Tzru-9ns8_w?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=3oQk0C), [notebook](---ThisDir---/zmiana_zmiennych_losowych_wolfram_language.nb)
    b) teoria: [nagranie](https://ujchmura-my.sharepoint.com/:v:/g/personal/kacper_topolnicki_uj_edu_pl/IQC3mFxBXlZ2TLUKvMblzK1yASLMDSEVbKgbxxUFcRV5_AU?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJPbmVEcml2ZUZvckJ1c2luZXNzIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXciLCJyZWZlcnJhbFZpZXciOiJNeUZpbGVzTGlua0NvcHkifX0&e=zhbvth), [notatki](---ThisDir---/zmiana_zmiennych_losowych.pdf)
7. YouTube:
    a) [3Blue1Brown, twierdzenie Bayesa 1](https://youtu.be/U_85TaXbeIo?si=SMrmKcbswmv4Lb71)
    b) [3Blue1Brown, twierdzenie Bayesa 2](https://youtu.be/HZGCoVF3YvM?si=d1c0Pb1I9AgZLq_d)
    c) [Veritasium, problemy 1](https://youtu.be/R13BD8qKeTg?si=wQyXEI_Yrd1VGhzJ)
    d) [Veritasium, problemy 2](https://youtu.be/42QuXLucH3Q?si=Ruep1yX8AQ0pFfDl)


