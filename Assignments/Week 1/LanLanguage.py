A=list(map(str,input().split()))
t=[0]*len(A)
str=["lios","liala","etr","etra","initis","inites"]

if len(A)==1:
    for i in str:
        if A[0].endswith(i):
            print("YES")
            exit(0)

    print("NO")
    exit(0)

for i in range(len(A)):
    for j in range(6):
        if A[i].endswith(str[j]):
            t[i]=j+1
            break

    #not belonging in any language
    if t[i]==0:
        print("NO")
        exit(0)

rem=t[0]%2
for i in range(len(t)):
    if t[i]%2!=rem:
        print("NO")
        exit(0)

x=sorted(t)
cnt=0


for i in range(len(t)):
    if t[i]==3 or t[i]==4:
        cnt+=1

    if t[i]!=x[i]:
        print("NO")
        exit(0)

if cnt==1:
    print("YES")

else:
    print("NO")
