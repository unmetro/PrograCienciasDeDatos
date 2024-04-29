
import nummpy as np

a = np.range(3) #imprime un vector de 0 al 2 de una dimension
a + 5 # seria un vector del 5,6,7


m = np.ones((3,3)) #imprime una matriz de 3x3 de puros 1s
a = np.arange(3) 
m + a #suma ese mismo vector de a a todas las filas de la matriz m

a = np.arange(3).reshape(3,1) #ahora la matriz tiene 3 filas y una columna en lugar de 1 fila y 3 columnas
b = np.arange(3)
a + b #suma no crea una matriz de 3x3 de 
"""
0,1,2
1,2,3
2,3,4

"""

m = np.ones((3,2)) #crea una matriz de 1s de 3 filas 2 columnas
a = np.arange(3) #crea una matriz de 0 al 2 como un vector

m.shape #imprime 3,2
a.shape #imprime 3
""""
primero paso del broadcasting
1-checar si tienen la misma dimension
2-modificar las dimensiones si no son iguales
3-aplicar el broadcasting 
"""

e = np.arange(4,15,2).reshape((3,2))
"""
4,6
8,10
12,14
"""
f = np.arange(3)

a = np.array([[4,5,7],[8,9,2]])
"""
4,5,7
8,9,2
"""
b = np.arange(3)