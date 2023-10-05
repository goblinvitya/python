words = input() + ' '
word = ''

for i in range(len(words)):
    if words[i] == ' ':
        word += words[i-1]

print(word)
