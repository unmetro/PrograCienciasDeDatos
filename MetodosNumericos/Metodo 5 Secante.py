
def funcion1(x):
    return (x-3)*(x+5)*(x-9)
  


def secante(pzero,puno,tol,iter):
    i = 2
    qzero = funcion1(pzero)
    quno = funcion1(puno)
    
    while( i <= iter):
        if((quno - qzero) == 0 ):
            return print("division por 0 no se puede")
        
        p = puno - quno*(puno - pzero)/(quno - qzero)
        
        if((p - puno) < tol ):
            return p
        
        i += 1
        
        pzero = puno
        qzero = quno
        pzero = p
        quno = funcion1(p)
    
    return 

print("METODO DE SECANTE")

print(secante(8,7,1000,1000))

    