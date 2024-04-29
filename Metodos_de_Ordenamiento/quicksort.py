
import random

def quicksort(arr, izq, der): #tiene el arreglo, luego tiene el principio y el final del arreglo
    if izq < der: 
        posparticion = particion(arr, izq, der)
        quicksort(arr, izq, posparticion - 1) #llamamos quicksort a todos los elemetnos que son menor a nuestro pivot
        quicksort(arr, posparticion + 1, der)#llamamos a quicksort a todos los elementos que son mayor a nuestro pivot
    return arreglo
    

def particion(arr, izq, der): #aqui declaramos nuestro pivot
    i = izq - 1 #iniciamos i que sea en -1 del inicio del arreglo
    pivot = arr[der] #nuestro pivot va a ser el ultimo elemento del arreglo

    for j in range(izq, der): #j va a ir por todo el arreglo
        #si el elemnto actual es menor al pivote
        if arr[j] < pivot:
            i += 1 #incrimenetamos i 
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            #intecambio de las posiciones del elemento i y j en el arreglo
        print(arreglo)
    
    #intercambio del pivote con el elemnto en la posicion i + 1      
    temp = arr[i + 1]
    arr[i + 1] = arr[der]
    arr[der] = temp
    return i + 1

arreglo = [x*3 for x in range(-15,10,2)]
random.shuffle(arreglo)
print(arreglo)

quicksort(arreglo, 0, len(arreglo)-1)
print(arreglo)
            
            
