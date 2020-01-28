import math
print("Wprowadz wspolczynnik a: ")
a = int(input())

print("Wprowadz wspolczynnik b: ")
b = int(input())

print("Wprowadz wspolczynnik c: ")
c = int(input())

print("Pierwsze miejsce zerowe: {0}/n Drugie miejce zerowe: {1}".format((-b+math.sqrt(b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)))