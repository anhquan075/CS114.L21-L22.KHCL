A={}
while True:
    x=list(map(int,input().split()))
    if x[0]==1: 
        A.update({x[-1]:x[0]})
    elif x[0]==0:
        break
    else:
        try:
            A[x[-1]]
        except KeyError:
            print("0")
        else:
            print("1")
          
