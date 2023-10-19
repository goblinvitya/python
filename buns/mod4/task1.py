def chars(ch):
    if len(set(ch)) == len(ch):
        return "Все числа разные"
    if ch.count(ch[0]) == len(ch):
        return "Все числа равны"
    return "Есть равные и неравные числа"


print(chars([1, 1, 3]))
