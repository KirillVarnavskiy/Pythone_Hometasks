# 7.1 Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.

song = input()
volwes = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
parts = song.split()
itog = list()
for item in parts:
    k = 0
    for letter in item:
        if letter in volwes:
            k += 1
    itog.append(k)
if len(set(itog)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')

