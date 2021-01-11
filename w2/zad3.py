suma = 0
print("Podaj pierwsza liczbe sumy")
n = int(input())
print("Podaj ostatnia liczbe sumy")
k=int(input())
for i in range(n,k+1):
    suma = suma + i
print("Wynik to " + str(suma))


def sumaelementow(n,k):
    suma = 0
    for i in range(n,k+1):
        suma=suma + i
    return suma