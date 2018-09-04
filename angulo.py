#Se necesita saber el valor del angulo entre dos vectores
import math

print('Dame el Primer Vector( componentes x, y, z)')
a1= float(input('Dame el valor de x1: '))
b1 = float(input('Dame el valor de y1: '))
c1 = float(input('Dame el valor de z1: '))
vector1 = [ a1, b1, c1 ]
print(vector1)
 
print('Dame el Segundo Vector( componentes x, y, z)')
a2 = float(input('Dame el valor de x2: '))
b2 = float(input('Dame el valor de y2: '))
c2 = float(input('Dame el valor de z2: '))
vector2 = [ a2, b2, c2 ]
print(vector2)
 
f = 180 / math.pi
g = (a1 * a2) + (b1 * b2) +(c1 * c2)
h = math.sqrt(( a1 ** 2 ) + ( b1 ** 2 ) +( c1 ** 2))
i = math.sqrt(( a2 ** 2 ) + ( b2 ** 2 ) +( c2 ** 2))
j = ( h * i )
k = math.acos((g)/(j))
angulo = f * k
print ('El angulo en grados entre los 2 vectores es: ' , angulo,)