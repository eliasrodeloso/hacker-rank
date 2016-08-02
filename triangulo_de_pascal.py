limite = int(input('Número de línea: '))
listaExt = []
for i in range(1, limite+1):
	listaInt = []
	for j in range(1, i+1):
		listaInt.insert(len(listaInt), j)
	if listaInt != []:
		print(listaInt)
	



