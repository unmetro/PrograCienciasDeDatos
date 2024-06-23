

import pandas as pd

serie = pd.Series([2,4,6,3,1])
serie 
# imprime un objeto de tipo series de la clase SERIES
"""
0 2
1 4
2 6
3 3
4 1
"""
#dtype: int64


#si fueramos a poner uno en flaot se pondrian todos en float
serie1 = pd.Series([2,4,6.2,3,1])
serie1
"""
0 2.0
1 4.0
2 6.2
3 3.0
4 1.0
"""
#dtype: float64
serie1.values
# imprime: array ([2. ,4. ,6.2,3. ,1. ])
serie1.index
# imprime: RangeIndex(starts=0,stop=5,step=1) empieza en 0, a cuantos lugares hay, que tanto incrementa


serie2 = pd.Series([i for i in range(1,11,2)],index = [2,4,7,3,1])
serie2
"""  cambio los indices, en lugar de empezar al 0 ahora cada uno tiene como un propio index
2 1
4 3
7 5
3 7
1 9
"""
serie2.index
# imprime: Index([2,4,7,3,1],dtypes'int64')
serie2mod = pd.Series([i for i in range(1,11,2)],index = [2,4,7,3,2])
serie2mod
"""  
2 1
4 3
7 5
3 7
2 9
"""
serie2mod[2]
#imprime:
"""  
2 1
2 9
"""


alumnos = pd.Series([10,9,8,7,6,5],index=['Yatziri','Marco','Diego','Ernesto','Rubi','Mario'])
alumnos
"""  
Yatziri 10
Marco 9
Diego 8
Ernesto 7
Rubi 6
Mario 5

dtype: int64
"""

alumnos.index
#imprime: Index(['Yatziri','Marco','Diego','Ernesto','Rubi','Mario'],dtype 'object')
alumnos['Diego']
#imprime: 8
alumnos.iloc[2] #accesar a los indices directamente
#imprime: 8

diccionario_inteligencia_perros = {'Salchica': 10,'Husky': 9,'Border Collie': 7,'Pastor Belga': 8} #tienen llave valor
inteligencia_perros = pd.Series (diccionario_inteligencia_perros)
inteligencia_perros
"""  
Salchicha 10
Husky 9
Border Collie 7
Pastor Belga 8

dtype: int64
"""
diccionario_color_perros = {'Salchica': 'Cafe','Husky': 'Negro/blanco','Border Collie': 'Blanco/negro','Pastor Belga': 'Cafe/negro'} #tienen llave valor
colores_perros = pd.Series(diccionario_color_perros)
colores_perros
"""  
Salchicha Cafe
Husky Negro/blanco
Border Collie Blanco/negro
Pastor Belga Cafe/negro

dtype: objet
"""

perros = pd.DataFrame({'inteligencia': inteligencia_perros, 'colores': colores_perros})
perros
