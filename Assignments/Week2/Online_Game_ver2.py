from sys import stdin
A=set()
while True:
    a = [int(i) for i in stdin.readline().split()]
    if len(a) == 0:
        continue

    x = a[0]    
    if x == 0:
        break
    elif x == 1:
        A.add(a[1])
    elif x==2:
        print(int(a[1] in A))   #ep kieu ve int de giong format de bai
    else:    
        A.discard(a[1])    
    