
import numpy as np

mm = 60*24*30
aleatorios = np.random.rand() #genera numeros random del 0 al 1
#es una matriz(vector) de 3 columnas 25 renglones

aleatorios.shape #te imprime la matriz que en este ejemplo seira (43200,3)
#son numeros con una distribucion uniforme 

#para poder hacer que sean numeros aleatorios del 1 al 10
aleatorios = aleatorios * 25 #ahora son del 0 al 25
aleatorios = aleatorios + 10 #ahora son del 10 al 35

#para poder calcular la media 
aleatorios.mean() #pero imprime el promedio de todo el tensor(osea toda la matriz)

#para poder tener de cada columna 
promedio_cuidad = aleatorios.mean(axis=0) #imprime la media de las columnas
promedio_minuto = aleatorios.mean(axis=1) #imprime la media de los renglones 

#para calcular la desviacion estandar(como estan distribuidos los datos)
de_cuidad = aleatorios.std(axis=0) 

#calcular normalizacion
normalizados = (aleatorios - promedio_cuidad)/de_cuidad
normalizados.mean(axis=0)
normalizados.std(axis=0) #datos estan centrados en 0 


# TODO_ESTO ES BROADCOASTING
