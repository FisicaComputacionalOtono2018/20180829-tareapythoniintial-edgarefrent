### Imprimir y contar los numeros multiplos de 3 que hay entre 1 y 100.
n = 1
h = 0
while n < 100:
    if n%3 == 0:
        print (n)
        h = h+n
    n=n+1
print ('La suma es:' ,h,)
