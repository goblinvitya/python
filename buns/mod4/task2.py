def pow(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow(a * a, n // 2)
    else:
        return a * pow(a, n - 1)


print(pow(4, 4))
