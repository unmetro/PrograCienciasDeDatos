
def funcion1(x):
    return (x-3)*(x+5)*(x-9)

def steff(pzero,tol,iter):
    
    i = 1
    
    while (i <= iter):
    
        puno = funcion1(pzero)
        pdos = funcion1(puno)
        p = pzero - ((puno - pzero)**2) / (pdos - 2*puno + pzero)
        
        if abs(p - pzero) < tol:
            print("Resultado exitoso")
            return p
        
        i += 1
        pzero = p

    return print("El metodo fallo despues de" ,iter, "iteraciones") 

print("METODO DE STEFFENSEN")
print(steff(9,100,100))
