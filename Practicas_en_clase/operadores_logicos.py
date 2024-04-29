
import numpy as np

aleatorios = np.random.randint(10) #crea nuemero aleatorio entero del 1 al 10
valores = np.random.randint(10,size = (5,5)) #crea una amtriz de 5x5 de numeros aleatorios del 1 - 10

valores == 0 #nos dice valores que sean iguales a 0 
#aqui solo me dice puros false y true

np.sum(valores == 0) #me imprime 3, que seria cuantos trues hay adentro de esta matriz

edades = np.random.randint(7,size(10,3))
edades = edades + 18 #esto me va a imprimir una matriz de 10x3 que tengan las edades entre 18 y 25

edades >= 20 #me dice truo o false a las edades que son mayor o igal a 20
edades <= 21 #los que son menor o igual a 21

(edades >= 20) & (edades <= 21) #me dice cuales estan entre edad j AND edad k
(edades < 19) | (edades > 23) #los que estan entre edad j OR edad k
np.sum(edades < 19) | (edades > 23) #me dice cuantos true hay adentro


