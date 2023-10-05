def check_duplicate_digits(sequence):
    digits = set()
    for num in sequence:
        for digit in str(num):
            if digit in digits:
                return True
            digits.add(digit)
    return False


sequence = input.split()
sequence = [int(num) for num in sequence]

result = check_duplicate_digits(sequence)
print(result)
