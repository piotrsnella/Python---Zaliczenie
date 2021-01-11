print("Wprowadz liczbe ktorej chcesz wyswietlic wszystkie dzielniki: ")
a = int(input())
for i in range (a):
    if a % (i+1) == 0:
        print ("Wprowadzona liczba jest podzielna przez:" + str(i+1))
    