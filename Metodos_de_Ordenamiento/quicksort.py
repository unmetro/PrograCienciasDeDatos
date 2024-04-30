import random

def quicksort(arreglo): #recibe un arreglo
    if len(arreglo) > 1: #si arreglo es mayor a 1 se ejecuta el codigo 
        pivot = arreglo[len(arreglo)//2] #establecemos nuestro pivote que es el elemento en la mitad
        arr_izq = [i for i in arreglo if i < pivot] #este arreglo almacena todos los elementos menores al pivote
        arr_mid = [i for i in arreglo if i == pivot] #este todos los elementos iguales al pivote
        arr_der = [i for i in arreglo if i > pivot] #este todos los elemetnos mayores al pivote
        return quicksort(arr_izq) + arr_mid + quicksort(arr_der) #es lo recursivo para que se llame a si misma concatenar
    return arreglo

lista = [i for i in range(0,15,2)]
random.shuffle(lista)
print(lista)

print(quicksort(lista))
