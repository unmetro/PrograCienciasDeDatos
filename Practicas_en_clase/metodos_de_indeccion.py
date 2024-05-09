import numpy as np


matriz = np.arange(1,26).reshape((5,5)) #hace una matriz d 5x5 que va del 1 al 25
#indexado simple 
matriz(2,3) #imprime el valor que esta en el renglon 2 fila 3
#slicing 
matriz[1:3, :] #imprimer los renglones 1 al 3, desde el principio al final
