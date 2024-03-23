def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        elemento_central = arr[0]
        menor_que_elemento_central = [x for x in arr[1:] if x <= elemento_central]
        mayor_que_elemento_central = [x for x in arr[1:] if x > elemento_central]
        return quick_sort(menor_que_elemento_central) + [elemento_central] + quick_sort(mayor_que_elemento_central)

# Ejemplo de uso:
arr = [3, 6, 8, 10, 1, 2, 1]
arr_ordenado = quick_sort(arr)
print("Arreglo ordenado:", arr_ordenado)

