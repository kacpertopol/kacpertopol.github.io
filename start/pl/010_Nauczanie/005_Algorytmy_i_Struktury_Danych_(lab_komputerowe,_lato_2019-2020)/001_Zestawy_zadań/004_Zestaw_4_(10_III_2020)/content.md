<center>
**A** 
</center>

<center>
(1 punkt)
</center>

Proszę zaimplementować ADT graph, który dla grafu $G$ oraz wierzchołków $x$, $y$ ma implementacje 
następujących operacji:

* $\text{adjacent}(G , x , y)$ - sprawdzanie, czy istnieje krawędź pomiędzy $x$ oraz $y$
* $\text{neighbours}(G , x)$ - zwracja sąsiadów $x$
* $\text{addVertex}(G , x)$ - dodaje $x$ do $G$
* $\text{removeVertex}(G , x)$ - usuwa $x$ z $G$
* $\text{addEdge}(G , x , y)$ - dodaje krawędź pomiędzy $x$ i $y$
* $\text{removeEdge}(G , x , y)$ - usuwa krawędź pomiędzy $x$ i $y$
* $\text{getVertexValue}(G , x)$ - zwraca wartość skojarzoną z $x$
* $\text{setVertexValue}(G , x , v)$ - kojarzy vartość $v$ z wierchołkiem $x$
* $\text{getEdgeValue}(G , x , y)$ - zwraca wartość skojarzoną z krawędzią pomiędzy $x$ oraz $y$
* $\text{setEdgeValue}(G , x , y , v)$ - kojarzy vartość $v$ z krawędzią pomiędzy $x$ oraz $y$

Państwa implementację proszę, na początek, oprzeć ma macierzy połączeń. Dodatkowo proszę zbadać złożoność 
jednej wybranej operacji (wykres oraz opis).
