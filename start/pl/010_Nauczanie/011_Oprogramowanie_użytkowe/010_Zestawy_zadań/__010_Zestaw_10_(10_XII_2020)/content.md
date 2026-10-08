<center>
**MATERIAŁY DODATKOWE**
</center>

- [twierdzenie Steinera](https://en.wikipedia.org/wiki/Parallel_axis_theorem)
- [moment bezwładności](https://en.wikipedia.org/wiki/Moment_of_inertia#Motion_in_space_of_a_rigid_body,_and_the_inertia_matrix)
- [chaotyczne notatki](---ThisDir---/notatki.pdf)

<center>
**A**
</center>

<center>
(2 punkty)
</center>

Korzystając z zadania **D** z zestawu 9 proszę przetestować 
[twierdzenie Steinera](https://en.wikipedia.org/wiki/Parallel_axis_theorem).
Aby to zrobić należy zdefiniować dwie identyczne bryły sztywne. Pierwsza jest umieszczona
tak aby jej środek masy pokrywał się z początkiem układu współrzędnych. 
Druga jest przesunięta, powiedzmy w kierunku osi *x*, o $\Delta$. Następnie 
można policzyć oraz porównać ich momenty bezwładności.

UWAGA: obydwie bryły powinny się mieścić w okienku zdefiniowanym w zadaniu **D** czyli 
$-1 \lt x \lt 1$ oraz $-1 \lt y \lt 1$.

<center>
**B**
</center>

<center>
(2 punkty)
</center>

Rozważamy sztywno względem siebie ułożone masy punktowe w trzech wymiarach:

<center>
![](---ThisDir---/cross.png)
</center>

Każdy punkt o numerze $i$ ma wapółrzędne $r_{i}$, masę $m_{i} = 1$ (dowolna jednostka masy), każde ramię krzyża ma długość
$2$ (dowolna jednosta odległości) a punkty są rozmieszczone co $0.2$ (dowolna jednostka odległości).

Proszę w mathematice skonstruować taki system, narysować go oraz policzyc momenty mezwładności:

$$I_{xx} = \sum_{1 = 1}^{N} m_{i} (y_{i}^{2} + z_{i}^{2})$$
$$I_{yy} = \sum_{1 = 1}^{N} m_{i} (x_{i}^{2} + z_{i}^{2})$$
$$I_{zz} = \sum_{1 = 1}^{N} m_{i} (x_{i}^{2} + y_{i}^{2})$$

$$I_{xy} = \sum_{1 = 1}^{N} m_{i} (x_{i} y_{i})$$
$$I_{xz} = \sum_{1 = 1}^{N} m_{i} (x_{i} z_{i})$$
$$I_{yz} = \sum_{1 = 1}^{N} m_{i} (y_{i} z_{i})$$

Wskazówka: Można skorzystać z `Riffle` , `Partition` , `Map` , `Union` , `Join` oraz `Table`.

<center>
**C**
</center>

<center>
(2 punkty)
</center>

Proszę policzyć macierz momentów bezwładności dla systemu z zadania **B**:

$$
I_{CM} = \left(
\begin{array}{ccc}
 I_{xx} & -I_{xy} & -I_{xz} \\
 -I_{xy} & I_{yy} & -I_{yz} \\
 -I_{xz} & -I_{yz} & I_{zz} \\
\end{array}
\right)
$$

Tym razem proszę skorzystać z zależności:

$$
I_{CM} = \sum_{i = 1}^{N} -m_{i} \left[\widetilde{r_{i}}\right].\left[\widetilde{r_{i}}\right]
$$

gdzie $\left[\widetilde{x}\right]$ jest macierzą reprezentującą operator liczenia iloczynu skalarnego z $x$.
Proszę ten wynik porównać z zadaniem **B**.

<center>
**D**
</center>

<center>
(2 punkty)
</center>


Proszę przesunąć wszystkie punkty systemu z zadania **B** o $1$ w kierunku $x$. Następnie proszę policzyć,
metodą z zadania **C**, macierz momentów bezwładności i porównać ją z macierzą liczoną z twierdzenia Steinera.
