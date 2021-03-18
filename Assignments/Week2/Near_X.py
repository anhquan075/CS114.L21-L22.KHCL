def findCrossOver(arr,low,high,x):
    if (arr[high] <= x):  
        return high 
          
    if (arr[low] > x):
        return low  
      
    mid = (low + high) // 2 

    if (arr[mid] <= x and arr[mid + 1] > x) : 
        return mid  
      
    if(arr[mid] < x) : 
        return findCrossOver(arr, mid + 1, high, x) 
      
    return findCrossOver(arr, low, mid - 1, x)

def FindValue(A, x, k):
    i = findCrossOver(A, 0, len(A)-1, x)
    low = i - 1
    high = i

    while k > 0:
        if low < 0 or (high < len(A) and abs(A[low] - x) > abs(A[high] - x)):
            high = high + 1
        else:
            low = low - 1
        
        k -= 1

    return(A[low+1: high])

n = int(input())
A = list(map(int,input().split()))[:n]
k,x = map(int,input().split())

Temp = FindValue(A,x,k)
for i in Temp:
    print(i, end=' ')