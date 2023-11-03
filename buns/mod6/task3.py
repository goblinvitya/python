def armstrong_numbers():
    for number in range(10, 10 ** 8):
        power = len(str(number))
        sum_of_digits = sum(int(digit) ** power for digit in str(number))
        if sum_of_digits == number:
            yield number


gen = armstrong_numbers()


def get_armstrong_numbers():
    return next(gen)


for i in range(8):
    print(get_armstrong_numbers(), end=' ')
