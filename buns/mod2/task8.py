data = input()
chars = data_input[len(data)-1:]
str = data_input[:len(data)-2]
count = 0

for i in str:
    if i == chars:
        count += 1
    else:
        break

print(count)
