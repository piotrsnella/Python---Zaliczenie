print("Jesli chcesz zmienic kilomentry na mile wpisz k, jesli odwrotnie wpisz m" )
decyzja = str(input())
if(decyzja == "k"):
    print("Wprowadz kilometry: ")
    a = float(input())
    mile = a * 0.62137
    print("Jest to " + str(mile) + " mil/i")
    
elif(decyzja == "m"):
    print("Wprowadz mile: ")
    b = float(input())
    km = b/0.62137
    print("Jest to " + str(km) + " kilometra")