import sys

a0,a1,a2 = input().strip().split(' ')
a = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b = [int(b0),int(b1),int(b2)]
A = 0
B = 0

for i in range(len(a)):
	if (a[i] >= 1 and a[i] <= 100) and (b[i] >= 1 and b[i] <= 100):
		if a[i] > b[i]:
			A = A + 1
		elif a[i] < b[i]:
			B = B + 1
			continue
		


print(str(A) + ' ' + str(B))
