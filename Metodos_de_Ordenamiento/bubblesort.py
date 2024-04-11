#bubble sort 3/4/2024

#def is how you define a function follow by the name and the type of data yor are gonna pass
def bsort(arreglo):
    n = len(arreglo)

    for i in range(0,n-2):
        for j in range(0,n-1):
            if arreglo[j] > arreglo[j+1]:
                temp = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = temp
    return arreglo
    

listaDesordenada = [8,7,1,4,3,2,1]

print(listaDesordenada)

listaOrdenada = bsort(listaDesordenada)

print(listaOrdenada)

print("Ya quedo el bubblesort")

print("holaaa")

