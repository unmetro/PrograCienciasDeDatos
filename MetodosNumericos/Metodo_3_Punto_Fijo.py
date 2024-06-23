
def funcion1(x):
    return (x-3)*(x+5)*(x-9)


def iteracion(aprox_in,tol,n):
    i = 1
    while( i < n):
        p = funcion1(aprox_in)
        if((p - aprox_in) < tol):
            return p
        
        i =+ 1
        aprox_in = p

    return

print(iteracion(2,0.000000001,100))