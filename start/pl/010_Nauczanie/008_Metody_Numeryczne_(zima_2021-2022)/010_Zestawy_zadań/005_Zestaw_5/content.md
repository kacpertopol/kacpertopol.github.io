<center>
**MATERIAŁY DODATKOWE**
</center>

[Notebook Mathematici](---ThisDir---/chol.nb) ilustrujący algorytm Cholesky'ego:

- wystarczy odpalić "Evaluate Notebook" i przyjrzeć się `Manipulate`
- zmienna `krok` to numer kroku algorytmu
- na niebiesko zaznaczone są wartości elementów macierzowych, których jeszcze nie znamy
- na czarno zaznaczone są wartości elementów macierzowych, które znamy na danym etapie algorytmu
- przykład zajmuje się macierzami 4x4 ale można go łatwo uogólnić

Ciekawostka, nieskończone macierze w Mathematice:

- [część 1](https://kacpertopol.github.io/myblog/2021-01-16_gen_light.html)
- [część 2](https://kacpertopol.github.io/myblog/2021-01-17_gen_light.html)
- [część 3](https://kacpertopol.github.io/myblog/2021-01-19_gen_light.html)


<center>
**A**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Znajdź faktoryzację Cholesky'ego macierzy:

$$
\left(
\begin{array}{cccccc}
 4 & 1 & 0 & 0 & 0 & 0 \\
 1 & 4 & 1 & 0 & 0 & 0 \\
 0 & 1 & 4 & 1 & 0 & 0 \\
 0 & 0 & 1 & 4 & 1 & 0 \\
 0 & 0 & 0 & 1 & 4 & 1 \\
 0 & 0 & 0 & 0 & 1 & 4 \\
\end{array}
\right)
$$

<center>
**B**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Znajdź faktoryzację Cholesky'ego macierzy:

$$
\left(
\begin{array}{cccccc}
 4 & 1 & 0 & 0 & 0 & 1 \\
 1 & 4 & 1 & 0 & 0 & 0 \\
 0 & 1 & 4 & 1 & 0 & 0 \\
 0 & 0 & 1 & 4 & 1 & 0 \\
 0 & 0 & 0 & 1 & 4 & 1 \\
 1 & 0 & 0 & 0 & 1 & 4 \\
\end{array}
\right)
$$

<center>
**C**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Niech $\mathbf{e} \in \mathbb{R}^{N}$, $||\mathbf{e}|| = 1$. Znajdź wektory i wartości własne macierzy

$$
\mathbf{P} = \mathbb{1} - 2 \mathbf{e} \mathbf{e}^{T}
$$

<center>
**D**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Dana jest macierz $\mathbf{A} \in \mathbb{R}^{N \times N}$ o następującej strukturze:

$$
\left(
\begin{array}{cccccccc}
 a_1 & b_1 & 0 & d_1 & 0 & \cdot  & \cdot  & \cdot  \\
 b_1 & a_2 & b_2 & 0 & d_2 & \cdot  & \cdot  & \cdot  \\
 0 & b_2 & a_3 & b_3 & 0 & \cdot  & \cdot  & \cdot  \\
 d_1 & 0 & b_3 & a_4 & b_4 & \cdot  & \cdot  & \cdot  \\
 0 & d_2 & 0 & b_4 & a_5 & \cdot  & \cdot  & \cdot  \\
 \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  \\
 \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  \\
 \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  & \cdot  \\
\end{array}
\right)
$$

Jest to macierz symetryczna, możemy na przyszłe potrzeby założyć, 
że jest także dodatnio określona.

- Czy jest to macierz rzadka? Dlaczego tak lub dlaczego nie? Zaproponuj *efektywny*
  sposób zapamiętywania tej macierzy.
- Niech $\mathbf{x} \in \mathbb{R}^{N}$ będzie wektorem. Korzystając z wyniku poprzedniego 
  podpunktu, zaproponuj *efektywny*, to znaczy unikający niepotrzebnych mnożeń przez zera,
  algorytm obliczania iloczynu $\mathbf{A} \mathbf{x}$, gdzie $\mathbf{A}$ jest macierzą w postaci
  jak na początku zadania i oszacuj złożoność obliczeniową tego algorytmu. Przedstaw stosowny kod w wybranym języku
  programowania lub pseudokod.
