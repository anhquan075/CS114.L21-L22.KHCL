n = int(input())	#Number of test case
A = []	#Contain result for every single test case
'''
n->0:
	input number of goods: m 
	array a[] to contain prices of each good
	If sum of all price can modulus m(goods) == 0 
		A[i] = sum(a) / m
	Else 
		A[i] = (sum(a) // m ) + 1 
	n--
'''
while n != 0:
	m = int(input())	
	a = list(map(int,input().split()))[:m] 
	if sum(a) % m == 0:
		A.append(int(sum(a) / m))
	else:
		A.append(sum(a) // m + 1)
	n = n - 1

for i in A:
	print(i)