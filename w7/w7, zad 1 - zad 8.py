import numpy as np
from collections import Counter 
import math 

def srednia(x):
    return sum(x) / len(x)

def median(x):
    x.sort()
    index = int(len(x)/2)
    if(len(x)%2 == 0):
        print(index)
        return (x[index-1]+x[index])/2 
    else:
        return x[index]
    
    
def dominant(x):
    c = Counter(x)
    return c.most_common(1) [0] [0]

def odchylenie(list):
    x = 0
    for i in list:
        x += (i - srednia(list))** 2
    return math.sqrt(x/len(list))

def wariancja(list):
    x = 0
    for i in list:
        x += (i - srednia(list))** 2
    return (x/len(list))

def skosnosc(list):
    x = 0
    for i in list:
        x += (i - srednia(list))** 3
    return (x/len(list))


def kurtoza(list):
    x = 0
    for i in list:
        x += ((i - srednia(list))** 4) - 3
    return (x/len(list))

def wspolczynnik_korelacji(list_1, list_2):
    sum1 = 0
    
    for i in range (len(list_1)-1):
        sum1 += list_1[i] * list_2[i]
        
    sum1 = sum1 * len(list_1)
    gora = sum1 - (sum(list_1) * sum(list_2))
    kw_x = 0 
    for i in list_1:
        kw_x += i**2
        
    return gora / ((len(list_1)* kw_x) - (sum(list_1)**2))
    






    
    