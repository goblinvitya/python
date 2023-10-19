def evq(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return evq(b, a % b)


print(evq(10, 15))