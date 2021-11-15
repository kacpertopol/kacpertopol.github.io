<center>
**MATERIAŁY DODATKOWE**
</center>

<center>
**A**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 4 punkt)
</center>

*Metoda gradientów sprzężonych*. Niech macierz $\mathbf{A} \in \mathbb{R}^{N \times N}$
będzie symetryczna i dodatnio określona. Niech $\mathbf{r}_{1} \in \mathbb{R}^{N}$
będzie dowolnym wektorem takim, że $||\mathbf{r}_{1}|| \ne 0$ i niech $\mathbf{p}_{1} = \mathbf{r}_{1}$.
Definiujemy następującą iterację:

$$\alpha_{k} = \frac{\mathbf{r}_{k}^{T} \mathbf{r}_{k}}{\mathbf{p}_{k}^{T} \mathbf{A} \mathbf{p}_{k}} \tag{1a}$$

$$\mathbf{r}_{k + 1} = \mathbf{r}_{k} - \alpha_{k} \mathbf{A} \mathbf{p}_{k} \tag{1b}$$

$$\beta_{k} = \frac{\mathbf{r}_{k + 1}^{T} \mathbf{r}_{k + 1}}{\mathbf{r}_{k}^{T} \mathbf{r}_{k}} \tag{1c}$$

$$\mathbf{p}_{k + 1} = \mathbf{r}_{k + 1} + \beta_{k} \mathbf{p}_{k} \tag{1d}$$

Udowodnij indukcyjnie, że dla każdych $i$, $j$, $i > j$, zachodzi (*)

$$\mathbf{r}_{i}^{T} \mathbf{r}_{j} = 0 \tag{2a}$$ 

$$\mathbf{r}_{i}^{T} \mathbf{p}_{j} = 0 \tag{2b}$$ 

$$\mathbf{p}_{i}^{T} \mathbf{A} \mathbf{p}_{j} = 0 \tag{2c}$$ 

Gdzie w dowodzie wykorzystuje się symetrię, gdzie zaś dodatnią określoność macierzy $\mathbf{A}$?

*Wskazówka*: Dowód należy przeprowadzić indukcyjnie. Krok indukcyjny polega na tym, iż zakładamy, że 
pierwsze $k < N$ wektorów $\mathbf{r}_{j}$, $\mathbf{p}_{j}$ spełnia (2). Następnie generujemy
wektory $\mathbf{r}_{k + 1}, \mathbf{p}_{k + 1}$. Trzeba pokazać, że one także spełniają (2)
korzystając z tego, że poprzednie wektory je spełniają. Dowód ten jest prosty, ale na ćwiczeniach
stracimy na niego mnóstwo czasu, jeśli nie *spróbujecie* go Państwo przeprowadzić samodzielnie.

<center>
**B**
</center>

<center>
\[[źródło: dr hab. Paweł Góra, prof. UJ](http://th-www.if.uj.edu.pl/zfs/gora/metnum21/)\]
</center>

<center>
(zadanie rachunkowe, 2 punkt)
</center>

Dane jest równanie liniowe:

$$\mathbf{A} \mathbf{x} = \mathbf{b} \tag{3}$$

przy czym macierz $\mathbf{A}$ spełnia założenia z poprzedniego zadania. Niech $\mathbf{x}_{1}$
będzie pierwszym (być może złym) przybliżeniem rozwiązania (3) i niech 
$\mathbf{r}_{1} = \mathbf{A} \mathbf{x}_{1} - \mathbf{b}$. W każdym kroku iteracji (1) definiujemy

$$\mathbf{x}_{k + 1} = x_{k} - \alpha_{k} \mathbf{p}_{k}. \tag{4}$$

Znaleźć związek pomiędzy $\mathbf{x}_{k}$ a $\mathbf{r}_{k}$. Pokazać, że $\mathbf{x}_{N + 1}$ jest ścisłym rozwiązaniem
równania (3) (w arytmetyce dokładnej).
