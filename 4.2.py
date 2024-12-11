import math

def calculate_series():
    S = 0  # Инициализация суммы
    for n in range(1, 11):
        # Вычисление a_n
        factorial_n = math.factorial(n)  # Вычисление факториала n!
        numerator = 2 * (factorial_n ** 2)  # Числитель: 2 * (n!)^2
        denominator = 3 * n + 1  # Знаменатель: 3n + 1
        a_n = numerator / denominator  # Формула для a_n
        S += a_n  # Добавление a_n к сумме
    return S

# Пример вызова
result = calculate_series()
print(f"Сумма десяти слагаемых ряда: {result}")
