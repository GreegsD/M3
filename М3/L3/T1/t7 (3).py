'''
Напишіть модуль, який допоможе Вам у математичних задачах, 
де потрібно знайти площу і периметр прямокутника.

На олімпіаді з математики виграє той, хто швидше за всіх вирішить завдання.
В одному із завдань потрібно знайти площу і периметр прямокутника. 
Давайте напишемо програму, яка буде містити дві функції: 
area () - повертає площу прямокутника, 
perimeter () - повертає периметр прямокутника.
Напишіть програму і збережіть її як модуль, 
який допоможе Вам у наступному завданні.
'''

# Напиши функцію perimeter () для обчислення периметра


# Напиши функцію area () для обчислення площі

# Збережіть цей код у файлі, наприклад, rectangle_module.py

def perimeter(length, width):
    """
    Обчислює периметр прямокутника.

    Параметри:
    length (float): Довжина прямокутника.
    width (float): Ширина прямокутника.

    Повертає:
    float: Периметр прямокутника.
    """
    return 2 * (length + width)

def area(length, width):
    """
    Обчислює площу прямокутника.

    Параметри:
    length (float): Довжина прямокутника.
    width (float): Ширина прямокутника.

    Повертає:
    float: Площа прямокутника.
    """
    return length * width

# Приклад використання модуля:

# Імпорт модуля
# з файлу rectangle_module.py
import rectangle_module

# Задання розмірів прямокутника
length = 5.0
width = 3.0

# Використання функцій з модуля
perimeter_result = rectangle_module.perimeter(length, width)
area_result = rectangle_module.area(length, width)

# Виведення результатів
print(f"Периметр прямокутника: {perimeter_result}")
print(f"Площа прямокутника: {area_result}")
