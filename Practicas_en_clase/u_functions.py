import numpy as np 

pares = np.range(2,21,2)
pares 

x = np.range(1,11) #un vector del 1 al 10
y = np.ones(10) #un vector de 10 1s
resultado2 = x+y
print(resultado2)

matriz1 = np.eye(5) #hace una matriz de 5x5 identidad
matriz2 = np.arange(1,26).reshape((5,5)) #hace una matriz d 5x5 que va del 1 al 25
#si queremos hacer un reshape y no tenemos los numeros suficientes no va a dar un error
#tiene dos tensores de dos dimensiones 

resultado3 = matriz1 + matriz2
print(resultado3)

2 ** matriz1 # aqui eleva 2 a la z de la matriz1 
-matriz2 #multiplico toda la matriz 2 por un -1

np.abs(m3) #funcion abs es valor absoluto

alpha = np.linspace(0,np.pi,10) #inicio,final,divisiones 
#linespace le das un intervalo, opera sobre el conjunto de los numereos reales
