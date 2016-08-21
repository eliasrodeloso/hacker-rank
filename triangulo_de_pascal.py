limite = int(input('Número de líneas: '))
listaExt = [[1], [1,1]]
for i in range(0, limite+1):
	listaInt = []
	for j in range(0, i):
		if i > 1:
			listaInt.append(j)
	listaExt.append(listaInt)
#Imprime el triangulo.
print("\nEmpieza el Triangulo de pascal:")
for k in listaExt:
	print(k)

arr = [1,2,3,4,10,11]
n = 0
for i in arr:
	n=n+i
print(n)
