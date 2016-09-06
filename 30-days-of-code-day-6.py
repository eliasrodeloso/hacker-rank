tc = int(input())
lista = []

if tc >= 1 and tc <= 10:
	for i in range(0, tc):
		string = input()
		lista.append(string)
	for j in lista:
		evens = []
		odds = []
		if len(j) >= 2 and len(j) <= 10000:
			for k in range(len(j)):
				if k % 2 == 0:
					evens.append(j[k])
				else:
					odds.append(j[k])
		print("".join(evens) + ' ' + "".join(odds))
