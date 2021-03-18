n,m=map(int,input().split())
arr=[]

for i in range(n):
    a1 = list(map(int,input().split()))[:m]
    arr.append(a1)

t,l,b,r=map(int,input().split())
x = [0]*m

trai = [0]*l
phai = [0]*(m- r-1)

for i in range(0, t):
    print(*x)

for i in range(t,b+1):
    print(*(trai + arr[i][l:r+1] + phai))

for i in range(b+1,n):
    print(*x) 


