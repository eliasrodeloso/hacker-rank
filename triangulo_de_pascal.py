limite = int(input('Hasta que linea desea trabajar?: \n'))
listaExt = list(range(limite))
for fila in listaExt:
	if fila == 1:
		print(fila)
	else:
		listaInt = list(range(fila))
		for columna in listaInt:
			print()