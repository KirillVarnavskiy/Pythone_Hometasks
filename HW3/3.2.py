# 2. Требуется определить ближайшее число к X в массиве A[1..N].

array = []
s = input("Введите длину списка: ")
s = int(s)
for i in range(s): 
    number = int(input()) 
    array.append(number)
print(array)
x = input("Введите интересующее число Х: ")
x = int(x)
result = min(array, key=lambda y: abs(x - y))
print(result)