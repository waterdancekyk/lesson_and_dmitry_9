from random import uniform
import numpy as np

def basic_solution():
    # Ввод данных
    n = int(input('Введите количество элементов: '))
    print('Введите пороговые значения:')
    a = float(input('a = '))
    b = float(input('b = '))


    mas = [uniform(a, b) for _ in range(n)]
    print("Исходный массив:")
    for el in mas:
        print(f"{el: 7.3f}", end=' ')
    print("\n")


    positive_elements = []
    for el in mas:
        if 0 < el <= 7:
            positive_elements.append(el)
    
    sum_positive = sum(positive_elements)
    count_positive = len(positive_elements)

    print(f"Сумма положительных элементов, не превосходящих 7: {sum_positive: 7.3f}")
    print(f"Количество положительных элементов, не превосходящих 7: {count_positive}")


    max_abs = abs(mas[0])
    min_abs = abs(mas[0])
    for el in mas:
        max_abs = max(max_abs, abs(el))
        min_abs = min(min_abs, abs(el))

    print(f"Максимальный по модулю элемент: {max_abs: 7.3f}")
    print(f"Минимальный по модулю элемент: {min_abs: 7.3f}")


    if n >= 3:
        mas[2] = max_abs + min_abs

    print("Обновленный массив:")
    for el in mas:
        print(f"{el: 7.3f}", end=' ')
    print("\n")



def advanced_solution():

    n = int(input('Введите количество элементов: '))
    print('Введите пороговые значения:')
    a = float(input('a = '))
    b = float(input('b = '))


    mas = [uniform(a, b) for _ in range(n)]
    print("Исходный массив:")
    print(' '.join(f"{el: 7.3f}" for el in mas))


    positive_elements = [el for el in mas if 0 < el <= 7]
    sum_positive = sum(positive_elements)
    count_positive = len(positive_elements)

    print(f"Сумма положительных элементов, не превосходящих 7: {sum_positive: 7.3f}")
    print(f"Количество положительных элементов, не превосходящих 7: {count_positive}")

    abs_values = [abs(el) for el in mas]
    max_abs = max(abs_values)
    min_abs = min(abs_values)

    print(f"Максимальный по модулю элемент: {max_abs: 7.3f}")
    print(f"Минимальный по модулю элемент: {min_abs: 7.3f}")


    if n >= 3:
        mas[2] = max_abs + min_abs

    print("Обновленный массив:")
    print(' '.join(f"{el: 7.3f}" for el in mas))


print("Выберите способ решения:\n1 - Базовый\n2 - Продвинутый")
choice = int(input("Ваш выбор: "))

if choice == 1:
    basic_solution()
elif choice == 2:
    advanced_solution()
else:
    print("Некорректный выбор!")
