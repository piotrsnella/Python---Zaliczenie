from pylab import plot

def f_lin(a,b):
    x = []
    y = []
    
    for i in range(0,11):
        x.append(i)
        y.append(x[i]*a+b)
    plot(x,y)
    return x,y

def f_kw(a,b,c):
    x=[]
    y=[]
    
    for i in range(0,11):
        x.append(i)
        y.append(x[i]**2*a + x[i]*b + c)
    plot(x,y)
    return x,y

def f_od(a,n):
    x=[]
    y=[]
    
    for i in range(0,11):
        print(i)
        x.append(i+1)
        y.append(a/(x[i]**n))
    plot(x,y)
    return x,y
