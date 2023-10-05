words = "кот гири док"

new_word = ''
for word in words:
    if word == ' ':
        continue
    new_word += word[-1]

print(new_word)