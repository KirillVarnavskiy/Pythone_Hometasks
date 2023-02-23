# 1. Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

array = []
s = input("Введите длину списка: ")
s = int(s)
for i in range(s): 
    number = int(input()) 
    array.append(number)
print(array)
x = input("Введите интересующее число Х: ")
x = int(x)
inc = 0
for i in array:
    if i == x:
        inc += 1
print(f'Число Х в списке встречается {inc} раз')


# array_numbers = [int(input()) for _ in range(int(input()))]
# print(array_numbers.count(int(input())))