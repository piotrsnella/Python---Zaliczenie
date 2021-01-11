print("Wprowadz liczbe: ")
a = float(input())
for i in range (10):
    c = float(a) * (i+1)
    print("{0} * {1} = {2}".format(float(a), i+1, float(c)))