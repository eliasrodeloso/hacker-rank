#Kangaroo
#
import sys

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

def findTheConstraints(x1,x2,v1,v2):
	isAboveZero = False
	isUnder = False
	if x1 <= 10000 and x2 <= 10000 and v1 <= 10000 and v2 <= 10000:
		isUnder = True
		if (x1 >= 0 and x2 >= 0) and (v1 >= 1 and v2 >= 1):
			isAboveZero = True
	if isUnder and isAboveZero:
		return True
	else:
		return False

def oneIsFaster(x1,x2,v1,v2):
	if x1 == x2 and v1 > v2:
		print('NO') 
	elif x1 <= x2 and v1 <= v2:
		print('NO')
	else:
		return False

if findTheConstraints(x1,v1,x2,v2):
	if oneIsFaster(x1,x2,v1,v2):
		print("NO")
	else:
		while True:
			x1 = x1 + v1
			x2 = x2 + v2
			if x1 == x2:
				print('YES')
				break

