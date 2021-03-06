n = int(input())
a = []

while n != 0:
	m = int(input())	
	a_lists = list(map(int,input().strip().split()))[:m] 
	if sum(a_lists) % m == 0:
		a.append(int(sum(a_lists) / m))
	else:
		a.append(sum(a_lists) // m + 1)
	n = n - 1

for i in a:
	print(i)