
lista = [x for x in range(1,11)]
lista2 = [x for x in range(10)]
lista3 = [x for x in range(-10,0,1)]

print(lista)
print(lista2)
print(lista3)
#slicing = obtener un segmento de una lista 
print("----------------")
print(lista[3:6])
print(lista[0:7])
print(lista[5:])
print(lista[:7])
print(lista[5:11])
print(lista[:-2])
print(lista[:]) # nomas dos puntos se refiere a toda la lista lista[:]
print("----------------")
posicionespares = lista[::2] 
print(posicionespares)
print(lista[::4])
print(lista[::-1])
print(lista[-2:1:-2])
print("------------")
# lista[x:y:z] x es donde empieza, y es donde termina, z el incremento 