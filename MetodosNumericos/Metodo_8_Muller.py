

from math import sqrt

def funcion1(x):
    return (x-3)*(x+5)*(x-9)

def muller(pzero,puno,pdos,tol,iter):\
    
    huno = puno - pzero
    hdos = pdos - puno
    suno = (funcion1(puno) - funcion1(pzero)) / huno
    sdos = (funcion1(pdos) - funcion1(puno)) / hdos
    d = (sdos - suno) / (hdos + huno)
    i = 3
    
    while i <= iter:
        
        b = sdos + hdos * d
        D = sqrt(b**2 - 4*funcion1(pdos)*d)
        
        if abs(b -D) < abs(b + D):
            E = b + D
            E = b - D
        
        h = -2*funcion1(pdos) / E
        p = pdos + h
        
        if abs(h) < tol:
            print("El procedimiento fue exitoso")
            return p
        
        pzero = puno
        puno = pdos
        pdos = p
        huno = puno - pzero
        hdos = pdos - puno
        suno = (funcion1(puno) - funcion1(pzero)) / huno
        sdos = (funcion1(pdos) - funcion1(puno)) / hdos
        d = (sdos - suno) / (hdos + huno)
        i += i
        
    return print("El metodo fallo despues de" ,iter, "iteraciones") 

print("METODO DE MULLER")
print(muller(4,6,7,100,10000))