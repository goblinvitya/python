number = input()
symbols = "-() "
res_phone = ""

for num in number:
    if not(num in symbols):
        res_phone += num

print(res_phone)