
import random

lista = [i for i in range(-10,15,3)]
random.shuffle(lista)
print("Esta es la primera lista")
print(lista)



#necesitamos ir una vez por cada elemento en la lista

def bsort(arreglo):
    for i in range(len(arreglo)): 
        #i representa cada elemento de la lista ya arreglada
        #al principio son 0 elementos ordenados, luego 1,2,3.....len que seria el total de elementos en la lista
        #compararar cada elemento que no esta ordenado y hacerle swap si es necesario
        for j in range(len(arreglo)-i-1): 
            #restandole i le dicimios que elementos faltan para arreglar y restandole el 1 es para no considerar el ultimo elemento
            if arreglo[j] > arreglo[j+1]:
                #si los elementos no estan en orden haz lo siguiente
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp           
    return arreglo
    

listaOrdenada = bsort(lista)

print("Ya quedo el bubblesort") 

print(listaOrdenada)


