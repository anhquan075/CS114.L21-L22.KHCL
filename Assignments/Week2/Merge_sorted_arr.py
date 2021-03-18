def mergeArrays(A, B, n, m):
    arr3 = [None] * (n + m)
    i = 0
    j = 0
    k = 0
 
    # Traverse both array
    while i < n and j < m:
        if A[i] < B[j]:
            arr3[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = B[j]
            k = k + 1
            j = j + 1
     
    while i < n:
        arr3[k] = A[i]
        k = k + 1
        i = i + 1
 
    while j < m:
        arr3[k] = B[j]
        k = k + 1
        j = j + 1
    
    for i in range(n + m):
        print(str(arr3[i]), end = " ")

n ,m = map(int,input().split())
A = list(map(int,input().split()))[:n]
B = list(map(int,input().split()))[:m]
mergeArrays(A,B,n,m)