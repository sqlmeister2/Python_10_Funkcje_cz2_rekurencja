
def func(x):
    return x * x

# bez nawiasów przy funkcji oznacza przypisanie funkcji do zmiennej, a nie przypisania jej wyniku
zmienna  = func
print(zmienna(5))

#przyjmowanie w argumencie funkcji f1
def func2(f1, x):
    return f1(x) * x # jasne wskazanie, że f1 jest funkcją

print(func2(func, 5))

#rekurencja w przykładzie z silnią
def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x-1)

print(silnia(5))

