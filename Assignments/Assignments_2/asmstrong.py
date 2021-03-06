n = int(input())

n_temp_1, n_temp_2 = n, n
count = 0
while n_temp_1 != 0:
    count = count + 1
    n_temp_1 = n_temp_1 // 10
 

count_temp = count
sum = 0
while count != 0:
    new_temp = n_temp_2 % 10
    sum = sum + new_temp**count_temp
    n_temp_2 = n_temp_2 // 10
    count = count - 1

print(True if sum == n else False)