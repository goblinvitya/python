num = int(input())
num1 = int(num)
num2 = int(num)
digits = "0123456789ABCDEF"

if num != int(num):
    print("Неверный ввод")
else:
    if num <= 0:
        print("Неверный ввод")
    else:
        binary = ''
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        octal = ''
        while num1 > 0:
            octal = str(num1 % 8) + octal
            num1 //= 8
        hexa = ''
        while num2 > 0:
            hexa = digits[num2 % 16] + hexa
            num2 //= 16
print(binary + ',', octal + ',', hexa)

