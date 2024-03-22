#mergesort Leo


def mergesort(arreglo):
    if len(arreglo) <= 1:
        return arreglo

    # Dividir el arreglo en mitades
    mitad = len(arreglo) // 2
    izquierdo = arreglo[:mitad]
    derecho = arreglo[mitad:]

    # Aplicar mergesort a ambas mitades
    izquierdo = mergesort(izquierdo)
    derecho = mergesort(derecho)

    # Combinar las dos mitades ordenadas
    return merge(izquierdo, derecho)

def merge(izquierdo1, derecho1):
    result = []
    i_izq = i_der = 0

    while i_izq < len(izquierdo1) and i_der < len(derecho1):
        if izquierdo1[i_izq] < derecho1[i_der]:
            result.append(izquierdo1[i_izq])
            i_izq += 1
        else:
            result.append(derecho1[i_der])
            i_der += 1

    # Agregar los elementos restantes de ambas mitades (si hay)
    result.extend(izquierdo1[i_izq:])
    result.extend(derecho1[i_der:])

    return result


arreglo = [12, 11, 13, 5, 6, 7,87,2,3,5]
print("Arreglo original:", arreglo)

arreglo = mergesort(arreglo)

print("Arreglo ordenado:", arreglo)
