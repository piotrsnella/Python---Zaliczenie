print("Podaj liczbe")
n = int(input())
def silnia_rek(n):
    if n> 1:
        return n * silnia_rek(n-1)
    elif n in (0,1):
        return 1
def silnia_ite(n):
    if n<2:
        return 1
    else:
        for i in range(2,n):
            n*=i
        return n
print(silnia_rek(n))
print(silnia_rek(n))
    
