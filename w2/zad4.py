print("Podaj ilosc elementow")
n = int(input())
tab=[]
print("Podaj dane")

for i in range(0,n):    
    tab.append(float(input()))

srednia = 0 
for i in range(0,len(tab)):
    srednia=(srednia + tab[i])
print("Srednia wynosi " + str(srednia/len(tab)))

    
