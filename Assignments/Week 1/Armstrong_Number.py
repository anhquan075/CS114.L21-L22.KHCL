def count_digit(x):
    count = 0
    while x > 0:
        x //= 10
        count += 1

    return count


def Is_Amrstrong(x):
    num = count_digit(x)
    tmp = x
    sum = 0

    while tmp > 0:
        last = tmp % 10
        tmp //= 10
        sum += (last**num)

    if sum == x:
        return True
    else:
        return False


n = int(input())

print(Is_Amrstrong(n))