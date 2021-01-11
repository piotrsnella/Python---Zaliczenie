while 1:
    print("Podaj liczbe punktów")
    punkt = float(input())
    procent = (punkt/40)*100
    if (procent<40):
        print("Twoja ocena to 1")
    elif (procent>40 and procent<50):
        print("Twoja ocena to 2")
    elif(procent>50 and procent<70):
        print("Twoja ocena to 3")
    elif(procent>70 and procent<84):
        print("Twoja ocena to 4")
    elif(procent>84 and procent<100):
        print("Twoja ocena to 5")
    else:
        print("Twoja ocena to 6")
    print("Chcesz sprawdzic kolejna ocene to wpisz cokolowiek, jesli zakonczyc wcisnij n")
    decyzja = input()
    if decyzja == "n":
        break
