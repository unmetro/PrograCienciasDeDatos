# import functools para toda la libreria
#lambda es una forma de hacer funciones cortas y anonimas, o sea no definirlas como tal
# filter es para filtrar los elementos de la lista que cumplan lo que estableces(lo que quieres evaluar, donde lo vas a evaluar)
#map es para lo que le aplicaras a toda la lista(lo que aplicaras, a donde lo vas aplicar)


#para mandar a llamar solo ciertas funciones de la libreria
from functools import reduce 


lista1=[]

for i in range (1,11):
  lista1.append(i)

print(lista1)

lista2 =list(map(lambda x: x*x, lista1))

print(lista2)

#filter. numeros pares
def par(x):
  #return x%
  
  if x%7==0:
    return True
  else:
    return False
    
  
lista3= list(filter(par,lista1))  

print(lista3)


lista4=list(filter(lambda x: x>6,lista1))
print(lista4)

lista5= list(filter(lambda x: x>30 and x<50, lista2))
print(lista5)

lista6= list(filter(lambda x: x<30 and x>50, lista2))
print(lista6)

precios =[20.0,18.0,35.0,40.0,2.0]

print(precios)

iva = list(map(lambda x: x*1.16,precios))

print(iva)

#reduce
def suma(x,y):
  return x+y

resultado= reduce(suma, lista1)

print(resultado)

factorial=reduce(lambda x,y: x*y,lista1)

print(factorial)