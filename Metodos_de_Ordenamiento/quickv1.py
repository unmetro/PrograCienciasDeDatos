# Lista inicial
lista = [2,9,8,7,4,5,6,3,0,1]

# Función para la separación del arreglo en partes menores, pivote y mayores
def separacion(lista):
    # Verifica si la lista está vacía
    if len(lista) < 1:
        return [], [], []
    
    # Listas para almacenar elementos menores, iguales y mayores que el pivote
    izq = [] 
    dere = []
    pivote = lista[0]  # Pivote es el primer elemento de la lista
    
    # Recorre la lista desde el segundo elemento
    for i in range(1, len(lista)):
        # Agrega elementos menores al pivote en la lista izquierda, 
        # y los demás en la lista derecha
        if lista[i] < pivote:
            izq.append(lista[i])
        else:
            dere.append(lista[i])
    
    # Retorna las listas de elementos menores, pivote y mayores
    return izq, pivote, dere

# Función de recursión para el algoritmo Quick Sort
def quicksort(lista):
    # Verifica si la lista tiene uno o ningún elemento
    if len(lista) < 2:
        return lista
    
    # Llama a la función separacion() para obtener las listas izquierda, pivote y derecha
    izq, pivote, dere = separacion(lista)
    
    # Recursivamente ordena las sublistas izquierda y derecha
    return quicksort(izq) + [pivote] + quicksort(dere)

# Imprime la lista original
print("Lista original:", lista)

# Ordena la lista utilizando el algoritmo Quick Sort
lista_ordenada = quicksort(lista)

# Imprime la lista ordenada
print("Lista ordenada:", lista_ordenada)
