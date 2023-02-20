# 2. Задача на числа Пети и Кати.

from math import sqrt
s = input("Enter the sum of numbers: ")
s = int(s)
p = input("Enter the product of numbers: ")
p = int(p)
z = sqrt( (s/2)**2 - p )
print( int( s/2 - z ), int( s/2 + z ) )