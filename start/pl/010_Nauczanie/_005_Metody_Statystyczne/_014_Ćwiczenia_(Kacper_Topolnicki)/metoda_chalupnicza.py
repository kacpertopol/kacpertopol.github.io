#!/usr/bin/env python3

import numpy as np
from scipy.stats import cauchy , uniform
import matplotlib.pyplot as plt

# Liczba danych do wylosowania z rozkładu Cauchiego:
n = 10000

# Parametry rozkładu Cauciego:
a , b = 0.5 , 1.5

# Dane wylosowane z rozkładu Cauciego:
data = cauchy.rvs(size = n , scale = b , loc = a)

# Funkcja implementujaca algorytm Metropolisa Hastingsa
def mhLog(nmh , data , da = 0.05 , db = 0.05 , a = 1.0 , b = 1.0):
    """
    nmh - liczba kroków w algorytmie Metropolisa Hastingsa
    data - [x0 , x1 , x2 , ...] dane obserwowane
    da , db - krok w parametrach a , b rozkładu Cauciego
    a , b - wstępne parametry rozkładu Cauciego
    """

    # W tych tabelkach bedziemy zapisywać wartości parametrów a , b:
    tracea , traceb = np.zeros(nmh + 1) , np.zeros(nmh + 1)
    tracea[0] = a
    traceb[0] = b

    # Uwaga 1: Ze względu na ograniczoną prezycję komputera
    # lepiej jest operować nie na wartościach funkcji gęstości
    # prawdopodobieństwa ale na logatytmach tych wartości.
    # Gdy potrzebujemy wartości prawdopodobieństwa wystarczy
    # policzyc eksponentę.

    # Uwaga 2: Zakładamy, że prior probability jest jednorodne
    # więc nie pojawia się w rachunkach. Przy dużej ilości
    # danych wybór prior probability nie powinien mieć większego
    # wpływu na końcowy wynik.

    # Uwaga 3: Logarytm zamiania mnożenie na dodawanie.
    # Suma elementów log(p(x0)) + log(p(x1)) + ...
    # to log(p(x0) * p(x1) * ...).

    accepted = 0.0

    logp = np.sum(cauchy.logpdf(data , loc = a , scale = b))
    for it in range(nmh):
        # Wybór nowych, próbnych, wartości parametrów rozkładu Cauciego:
        newa = a + uniform.rvs(loc = -da , scale = 2.0 * da)
        newb = b + uniform.rvs(loc = -db , scale = 2.0 * db)
        
        # Logarytm z gęstości prawdopodobieństwa dla nowych parametrów
        # rozkładu Cauchiego:
        newlogp = np.sum(cauchy.logpdf(data , loc = newa , scale = newb))
        
        # Prawdopodobieństwo akceptacji nowych parametrów rozkładu
        # Cauchiego:
        acc = min(1.0 , np.exp(newlogp - logp))
        if uniform.rvs(loc = 0.0 , scale = 1.0) < acc:
            a = newa
            b = newb
            logp = newlogp
            accepted += 1.0

        # Zapis aktualnych wartości rozkładu Cauchiego:
        tracea[it + 1] = a
        traceb[it + 1] = b

    print("fraction accepted : " , accepted / nmh)

    return tracea , traceb

# Liczba kroków w algorytmie Metropolisa Hasingsa:
nmh = 10000

# Uruchomienie algorytmu Metropolisa Hastingsa.
# Zakładamy wstępnie, że parametry rozkładu Cauchiego
# a = 1.0 , b = 1.0:
tracea , traceb = mhLog(nmh , data , a = 1.0 , b = 1.0)

# Rysowanie przebiegu algorytmu Metropolisa Hastingsa:
plt.plot(tracea , label = "a")
plt.plot(traceb , label = "b")
plt.legend()
plt.show()

# Z rysunków wynika, że warto wyrzucić około 2000 pierwszych iteracji:
tm = 5000

# Histogramy parametrów:
plt.hist(tracea[tm:] , label = "a")
plt.hist(traceb[tm:] , label = "b")
plt.legend()
plt.show()
