numbers = input()
ind = numbers.find(" ")
ind2 = numbers.find(" ", ind + 1)
a = int(numbers[:ind])
b = int(numbers[ind+1:ind2])
c = int(numbers[ind2+1:])

if (a > b):
    if (c > a):
        print(a)
    elif (c > b):
        print(c)
    else:
        print(b)
elif(c > b):
    print(b)
else:
    if (a > c):
        print(a)
    else:
        print(c)
