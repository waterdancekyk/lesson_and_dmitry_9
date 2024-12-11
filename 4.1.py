import math

def calculate_and_compare(x, y, z):
    # Проверка области допустимых значений
    if x + 1 <= 0:
        return "Ошибка: логарифмируемое выражение (x+1) должно быть больше 0."
    if z < 0:
        return "Ошибка: подкоренное выражение z должно быть неотрицательным."
    if abs(x + y) - math.sqrt(z) == 0:
        return "Ошибка: знаменатель дроби равен нулю."

    # Вычисление a и b
    try:
        a = math.cos(math.pi / 4 + x) * math.sqrt(x**2 + y**2 + z**2)
        b = math.log(x + 1) / (abs(x + y) - math.sqrt(z))
    except ValueError as e:
        return f"Ошибка вычислений: {e}"
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."

    # Сравнение
    if a > b:
        comparison = "a > b"
    elif a < b:
        comparison = "a < b"
    else:
        comparison = "a = b"

    return f"a = {a}, b = {b}, результат: {comparison}"

# Пример вызова
x, y, z = 1, 2, 3
result = calculate_and_compare(x, y, z)
print(result)
