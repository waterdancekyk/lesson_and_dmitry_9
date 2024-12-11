# Инициализация матрицы 5x5
matrix = [
    [10, 15, 20, 25, 30],
    [5, 7, 10, 12, 20],
    [15, 18, 30, 25, 35],
    [9, 5, 15, 40, 50],
    [100, 3, 25, 55, 10]
]

# Функция для подсчета количества элементов, кратных 5 в каждой строке
def count_multiples_of_5(matrix):
    for i in range(len(matrix)):  # Для каждой строки
        count = 0  # Счетчик элементов, кратных 5
        for j in range(len(matrix[i])):  # Для каждого элемента в строке
            if matrix[i][j] % 5 == 0:
                count += 1
        print(f"Строка {i+1}: {count} элементов кратных 5")

# Модификация матрицы (например, умножить элементы, кратные 5, на 2)
def modify_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 5 == 0:
                matrix[i][j] *= 2  # Умножаем элемент на 2

# Вызов функций
count_multiples_of_5(matrix)
modify_matrix(matrix)

# Вывод измененной матрицы
print("\nИзмененная матрица:")
for row in matrix:
    print(row)
