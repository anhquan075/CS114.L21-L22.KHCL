from collections import Counter


q = int(input())

for i in range(q):
	n, m = map(int, input().split())
	lst = list(map(int,input().strip().split()))[:n] 
	print(Counter(lst)[m])