q = int(input())
result = []

for k in range(q):
  s = input()
  t = input()
  flag = False


  for i in s:
    if flag == False:
      for j in t:
        if i == j:
          flag = True
          

    else:
      break

  if flag == True:
    result.append('YES')
  else:
    result.append('NO')

for i in result:
    print(i)