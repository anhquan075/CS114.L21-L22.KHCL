t = int(input())

for i in range(t):
    n = int(input())
    if n == 2:
        print('2')
    elif n % 2 == 0:
        print('0')
    else:
        print('1')