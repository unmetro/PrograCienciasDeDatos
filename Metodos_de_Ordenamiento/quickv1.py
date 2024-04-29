#ALAN DANIEL PALMA PACHECO QUICK SORT

#DEFINE UNA LISTA
lista = [2,9,8,7,4,5,6,3,0,1]

#CREAR FUNCIONE PARA EL METODO DE ORDENAMIENTO 
def separacion(lista):
    if len(lista) < 1:
        return [], [], []
    
    #DE AMBAS PARTES AL HACER LA SEPARACION SE TIENE QUE ESTAR
    izq = [] 
    dere = []
    pivote = lista[0]
    
    #RECORRER EL ARREGLO 
    for i in range(1, len(lista)):
        if lista[i] < pivote:
            izq.append(lista[i])
        else:
            dere.append(lista[i])
    
    return izq, pivote, dere

#FUNCION DE RECURSION PARA EL ARREGLO 
def quicksort(lista):
    if len(lista) < 2:
        return lista
    
    izq, pivote, dere = separacion(lista)
    return quicksort(izq) + [pivote] + quicksort(dere)

print(quicksort(lista))
