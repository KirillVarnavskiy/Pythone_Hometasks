# 1. Найдите сумму цифр трехзначного числа.

n = input("Enter three-digit number:")
n = int(n)
a = n // 100
b = n // 10 % 10
c = n % 10
print(a + b + c)