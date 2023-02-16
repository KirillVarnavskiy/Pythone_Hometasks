# 4. Задача на деление шоколадки

print("Enter the chockolate size (n*m) and the number of chockolate's segments: ")
n = int(input())
m = int(input())
k = int(input())

if k < m*n and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')