# # Day 1
# i = 4
# d = 4.0
# s = 'HackerRank '
# inte=0
# dou=0.0
# st=''

# def suma(ent1,ent2):
# 	return ent1+ent2

# inte=int(input(''))
# dou=float(input(''))
# st=input('')

# print(suma(inte,i))
# print(suma(d,dou))
# print(s+st)

# #Day 2
# mealCost = 0
# tipPercent = 0
# taxPercent = 0
# totalCost = 0

# mealCost = float(input(''))
# tipPercent = int(input(''))
# taxPercent = int(input(''))

# def findTip(mealCost,tipPercent):
# 	percent = 100
# 	return mealCost*(tipPercent/percent)

# def findTax(mealCost, taxPercent):
# 	percent = 100
# 	return mealCost*(taxPercent/percent)

# def findTotal(mealCost, tip, tax):
# 	return int(round(mealCost + tip + tax,0))

# tip = findTip(mealCost,tipPercent)
# tax = findTax(mealCost,taxPercent)
# totalCost = str(findTotal(mealCost,tip,tax))

# print('The total meal cost is '+totalCost+' dollars.')

# #Day 4:
# class Person:
  
#   def __init__(self,initialAge):
#   	if not initialAge > 30 and initialAge >= -5:
#   		if initialAge < 0:
# 	  		print('Age is not valid, setting age to 0.')
# 	  		self.age = 0
# 	  	else:
# 	  		self.age = initialAge

#   def amIOld(self):
#   	if self.age < 13:
#   		print('You are young.')
#   	elif self.age >= 13 and self.age < 18:
#   		print('You are teenager.')
#   	else:
#   		print('You are old.')
      
#   def yearPasses(self):
#   	self.age = self.age + 1

# # Day 5:
# import sys

# n = int(input().strip())

# if n >= 2 and n <= 20:
# 	for i in range(1,11):
# 		print(str(n) +' x '+ str(i) +' = ' +str(n*i))

# Day 6
# tc = int(input())
# lista = []

# if tc >= 1 and tc <= 10:
# 	for i in range(0, tc):
# 		string = input()
# 		lista.append(string)
# 	for j in lista:
# 		evens = []
# 		odds = []
# 		if len(j) >= 2 and len(j) <= 10000:
# 			for k in range(len(j)):
# 				if k % 2 == 0:
# 					evens.append(j[k])
# 				else:
# 					odds.append(j[k])
# 		print("".join(evens) + ' ' + "".join(odds))


#Day 7: Arrays

# import sys

# n = int(input().strip())

# if n >= 1 and n <= 1000:
# 	arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
# 	lista = []
# 	k = len(arr)
# 	for i in range(k,0,-1):
# 		lista.append(str(arr[i-1]))
# 	print(" ".join(lista))

# Day 8: Dictionaries and Maps
# 
# import sys

# n = int(input())
# phoneBook = {}
# if n >= 1 and n <= 10**5:
# 	for i in range(n):
# 		dato = input('').split()
# 		phoneBook[dato[0]] = dato[1]

# 	queries = sys.stdin.readlines()
# 	for query in queries:
# 		name = query.strip()
# 		if name in phoneBook:
# 			print(name + "=" + str(phoneBook[name]))
# 		else:
# 			print("Not found")

#Day 9: Recursión
#
def factorial (n):
	if n-1 >= 1:
		return n*factorial(n-1)
	else:
		return n

print(factorial(int(input())))