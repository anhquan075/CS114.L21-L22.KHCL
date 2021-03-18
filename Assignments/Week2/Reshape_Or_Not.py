from sys import stdin

m , n = [int(i) for i in input().split()]
r, c = [int(i) for i in input().split()]

if r*c != m*n:
    for i in range(m):
        q = input()
        print(q)
else:
    arr = []
    j =0
    for i in range(m):
        q = input()
        arr += q.split(" ")
        
        if (len(arr) > c):
            print(*arr[:c])
            arr = arr[c:]
            j+=1
    
    for x in range(0, r-j):
        print(*arr[x*c:x*c+c])