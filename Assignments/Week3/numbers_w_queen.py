n,m = map(int,input().split())
x = 1
cnt = 0
while x <= n:
  x = x*10
cnt = m // x
if m%x >= n:
  cnt+=1
print(cnt)