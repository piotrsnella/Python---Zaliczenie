from pylab import plot, show, xticks, yticks, savefig
def lista (a,b,c):
    x = [1,2,3,4,5,6,7,8,9]
    y=[]
    for var in x:
        value = (a**var)+(b*var)+c
        y.append(value)
        

    return x,y


def lista2 (a,b,c):
    x=[]
    y=[]
    
    for i in range (0,100):
        x.append(i)
        y.append(a*x[i]**2+ b*x[i]+c)
        
    return x,y

def lista3 (a,p,q):
    x=[]
    y=[]
    for i in range (0,100):
        x.append(i-50)
        y.append(a*(x[i]-p)**2+q)
        
    return x,y

def wykres():
    for i in range (1,10):
        lista3(i,i,i)
        plot(x,y)
        show()
        savefig("wykres" + str(i)+ ".png")
        