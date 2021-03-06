from math import ceil
#ceil return the smallest integer not less than x
n, m, a = map(int, input().split())
print(int(ceil(n/a)*ceil(m/a)))
