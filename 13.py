def silnia(x):
    if x>1:
        return x*silnia(x-1)
    elif x in (0,1):
        return 1

def newton(n, k):
    return silnia(n)/(silnia(k) * silnia(n-k))

def loop():
    n = int(input("Podaj n: "))
    k = int(input("Podaj k: "))

    print(f'Wynik: {newton(n, k)}')
    
    wybor = input("Czy chcesz kontynuować? (Y/N)")
    
    if wybor == "Y" or wybor == "y":
        loop()
    else:
        quit()

loop()
