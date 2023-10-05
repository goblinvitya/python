s = input()

vowels = 'аеёиоуыэюя'
consonants = 'бвгджзйклмнпрстфхцчшщ'

vowel_count = 0
consonant_count = 0

for char in s:
    if char.lower() in vowels:
        vowel_count += 1
    elif char.lower() in consonants:
        consonant_count += 1

print(vowel_count, consonant_count)
