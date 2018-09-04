#Calcular los 3 angulos de un vector en 3 dimensiones
import math

print('Dame las componentes x, y, z del vector')
a1=float(input('Dame el valor de x: '))
a2=float(input('Dame el valor de y: '))
a3=float(input('Dame el valor de z: '))
vector=[a1, a2, a3]

c=180/math.pi
d=math.sqrt((a1**2)+(a2**2)+(a3**2))
a=math.acos((a1)/(d))
b=math.acos((a2)/(d))
g=math.acos((a3)/(d))

alfa=a*c
beta=b*c
gama=g*c

print('El angulo del vector con el eje x es:',alfa,)
print('El angulo del vector con el eje y es:',beta,)
print('El angulo del vector con el eje z es',gama,)