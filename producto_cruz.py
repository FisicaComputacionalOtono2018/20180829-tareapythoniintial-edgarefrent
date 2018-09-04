#Calcular el producto vectorial de dos vectores

import math

print('Dame las componentes x, y, z del Vector 1')
a1=float(input('Dame el valor de la componente x1: '))
a2=float(input('Dame el valor de la componente y1: '))
a3=float(input('Dame el valor de la componente z1: '))
vector1=[a1, a2, a3]
print(vector1)

print('Dame las componentes del Vector 2')
b1=float(input('Dame el valor de la componente x2: '))
b2=float(input('Dame el valor de la componente y2: '))
b3=float(input('Dame el valor de la componente z2: '))
vector2=[b1, b2, b3]
print(vector2)

x=(a2*b3)-(a3*b2) 
y=-((a1*b3)-(a3*b1))
z=(a1*b2)-(b1*a2) 

f=math.sqrt((x**2)+(y**2)+(z**2))

print('El producto vectorial del Vector 1 por el Vector 2 es el Nuevo Vector con magnitud:',f,)
print('Con componente en x:',x,)
print('Componente y:',y,)
print('Componente z:',z,)