from random import randint , choice

def run_game(strategy = False):
    car = randint(1 , 3)
    initial = randint(1 , 3)
    shown = choice(list({1 , 2 , 3}.difference({car , initial})))
    possibility = list({1 , 2,  3}.difference({initial , shown}))[0]
    if strategy:
        return int(possibility == car)
    else:
        return int(initial == car)

n = 10000000

without_change = 0
for i in range(n):
    without_change += run_game(strategy = False)
print("without change :" , without_change / n)

without_change = 0
for i in range(n):
    without_change += run_game(strategy = True)
print("without change :" , without_change / n)
