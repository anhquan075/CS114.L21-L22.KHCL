k=[int(x) for x in input().split()]
arr=[[] for _ in range(k[0]+1)]

for i in range(k[0]):
    arr[i] = [int(j) for j in input().split()]

for j in range(k[1]):
       arr[k[0]].append(max(len(str(arr[i][j])) for i in range(k[0])))

for i in range(k[0]):
   for j in range(k[1]):
        if j!=k[1]-1:
           print(str(arr[i][j]).rjust(arr[k[0]][j]), end=" ")
        else :
            print(str(arr[i][j]).rjust(arr[k[0]][j]))