# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

mas = [2, 4, 2, 6, 3, 1, 5, 1, 6]

print(*mas)

maxi=int(input("MAX= "))

mini=int(input("MIN= "))

masi=[]

if maxi>=mini:

   for i in range(len(mas)):

      if maxi>=mas[i] and mini<=mas[i]:

          masi.append(i)

   print("Кол-во:",len(masi))

   print("Индексы:",masi)