import math

t = int(input())

for i in range(t):
    n, m = map(int ,input().split())
    if m < 0 :
        print(n)
    else:
    	if n % m == 0:
    		print(n // m)
    	else:
        	print(n//math.gcd(n,m), m//math.gcd(n,m))
