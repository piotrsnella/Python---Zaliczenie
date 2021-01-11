print("Jesli chcesz zmienic Celcjusze na Fahrenheita wpisz c, jesli odwrotnie wpisz f")
decyzja = str(input())
if(decyzja == "c"):
    print("Wprowadz Celcjusze: ")
    a = float(input())
    fahr = (a*9/5)+3
    print("Jest to " + str(fahr) + "stopni Fahreheinta")
    
elif(decyzja == "f"):
     print("Wprowadz stopnie Fahrenheita: ")
     b = float(input())
     celc = (b-32)*(5/9)
     print("Jest to " + str(celc) + "stopni Celcjusza")