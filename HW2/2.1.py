# 1. Задача на монеты

n = input("Enter the number of coins: ")
n = int(n)
k = 0
print("Enter in order the coins turned tails ('1') and the coins turned with the coat of arms ('0')")
for i in range(n):
    v = int(input())
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)
