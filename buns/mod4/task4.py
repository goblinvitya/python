def palindrome(word):
    count1 = {}
    for char in word:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1

    count2 = 0
    chars = ''
    palindromes = ''

    for char in count1:
        if count1[char] % 2 != 0:
            count2 += 1
            if count2 > 1:
                return "Невозможно сформировать палиндром из данного слова."
            else:
                chars = char

        for _ in range(count1[char] // 2):
            palindromes += char

    return palindromes + chars + palindromes[::-1]


print(palindrome("мадам"))