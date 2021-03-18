from sys import stdin,stdout
A = []

while True:
    l = [int(i) for i in stdin.readline().split()]
    if l[0] == 0:
        A.insert(0,l[1])
    
    elif l[0] == 1:
        A.append(l[1])
    
    elif l[0] == 2:
        if l[1] in A:
            A.insert(A.index(l[1]),l[2])
        else:
            A.insert(0,l[2])
    
    elif l[0] == 3:
        if l[1] in A:
            A.remove(l[1])
    
    elif l[0] == 4:
        while l[1] in A:
            A.remove(l[1])
    
    elif l[0] == 5:
        if ans:
            A.pop(0)
    
    else:
        break
print(*A)