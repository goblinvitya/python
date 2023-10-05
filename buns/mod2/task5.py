numbers = input()
i = 0
n = 0
counter = 0

for char in numbers:
    if char == ',':
        i = str(numbers[:counter])
        n = int(numbers[counter + 2:])
    counter += 1

a_num = ord(i)

k_num = a_num + n

if k_num < 97:
    k_num = 122 - (96 - k_num) % 26
elif k_num > 122:
    k_num = 96 + (k_num - 122) % 26

k = chr(k_num)

print(k)