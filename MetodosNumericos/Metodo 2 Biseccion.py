
def funcion1(x):
    return (x-3)*(x+5)*(x-9)

def funcion2(x):
    return (x-9)*(x+99)*(x-6)*(x-8)*(x-13)

def funcion3(x):
    return (x-1j)*(x+1j)*(x-1)*(x-9)

def funcion4(x):
    return x+3



def biseccion(a,b,tol,N):
    i = 1
    Fa = funcion4(a)
    while(i <= N):
        p = a + (b-a)/2
        Fp = funcion4(p)
        if(Fp == 0 or (b-a)/2 < tol):
            return p
        i =+ 1
        if(Fa*Fp > 0):
            a = p
            Fa = Fp
        else:
            b = p
    return

#ij
print(biseccion(-9,100,0.000000000001,100))