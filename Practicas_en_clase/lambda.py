
#hay para crear funciones anonimas
#lamba function

f = lambda x: x*x

print(f(5))

f2 = lambda x,y: x+y

print(f2(3,4))

lista1 = []
for i in range(1,11):
    lista1.append(i)

print(lista1)

lista2 = list(map(lambda x: x*x,lista1))
print(lista2)

#filter, numeros pares

def par(x):
    if x%7 == 0:
        return True
    else:
        return False

lista3 = list(filter(par,lista1))
print(lista3)

lista4 = list(filter(lambda x: x>6,lista1))
print(lista4)

lista5 = list(filter(lambda x: x>30 and x<50,lista2))
print(lista5)


precios = [20.0, 18.0, 35.0, 40.0, 2.0]

print(precios)

iva = list(map(lambda x: x*1.16,precios))
print(iva)