import random

arreglo = [i for i in range(7)]
random.shuffle(arreglo)
print(arreglo)

def mergesort(arreglo):
    if len(arreglo) > 1:
        arr_iq = arreglo[:len(arreglo)//2] #aqui regresa el arrelgo original pero corotado, empezando de 0 hasta la mitas
        arr_der = arreglo[len(arreglo)//2:] #aqui regresa el arrelgo original pero empezando desde la mitad hasta el tamanio del arreglo n
        
        #nuestra recursion
        mergesort(arr_iq)
        mergesort(arr_der)
        if len(arreglo) == 7:
            print(arr_iq)
            print(arr_der)
        #implementamos el merge
        i = 0 #para estar concientes del valor mas izquierdo del arreglo
        j = 0 #valor mas derecho del arreglo
        k = 0 #index del merge
        while i < len(arr_iq) and j < len(arr_der):
            if arr_iq[i] < arr_der[j]:
                arreglo[k] = arr_iq[i]
                i += 1
                k += 1
            else:
                arreglo[k] = arr_der[j]
                j += 1
                k += 1
                
        while i < len(arr_iq):
            arreglo[k] = arr_iq[i]
            i += 1
            k += 1
        
        while j < len(arr_der):
            arreglo[k] = arr_der[j]
            j += 1
            k += 1
    return arreglo
            
mergesort(arreglo)
print(arreglo)
        