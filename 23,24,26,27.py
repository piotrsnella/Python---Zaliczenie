import numpy as np
from collections import Counter 
import math 
#x = int(input())
def srednia(x):
    return sum(x) / len(x)
    
def dominant(x):
    c = Counter(x)   
    return c.most_common(1) [0] [0]

def odchylenie(list):
    x = 0
    for i in list:
        x += (i - srednia(list))** 2 
    return math.sqrt(x/len(list))


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

