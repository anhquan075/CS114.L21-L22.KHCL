import math

n = int(input())

for i in range(n):
    a, b = map(int ,input().split())
    if b < 0 :
        print(a)
    else:
    	if a % b == 0:
    		print(a // b)
    	else:
        	print(a//math.gcd(a,b), b//math.gcd(a,b))