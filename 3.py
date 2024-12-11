from random import randint


M = int(input("Введите количество строк (M): "))
N = int(input("Введите количество столбцов (N): "))


A = [[randint(10, 99) for _ in range(N)] for _ in range(M)]


print("\nМатрица:")
for row in A:
    print(" ".join(f"{x:3}" for x in row))


count = 0
for row in A:
    if all(x % 10 != 0 for x in row):  
        count += 1


print(f"\nКоличество строк, где последняя цифра всех элементов отличается от нуля: {count}")
