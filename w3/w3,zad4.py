import matplotlib.pyplot as plt 

def f_lin(a,b):
    x = []
    y = []
    
    for i in range(0,11):
        x.append(i)
        y.append(x[i]*a+b)
    plt.plot(x,y)
    return x,y

for i in range(15):
    x, y = f_lin(i, i *2)
    plt.figure()
    plt.plot(x,y)
    plt.savefig("foto_{0}".format(i))