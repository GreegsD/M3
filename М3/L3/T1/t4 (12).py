'''
Давайте допоможемо фізикам перевести час в секунди!

Коли вчені-фізики виконують експеримент, 
витрачений на нього час вимірюється в секундах, 
навіть якщо дослід тривав більше декількох годин. 
Давайте полегшимо життя фізикам і напишемо програму, 
яка буде переводити витрачені години та хвилини в секунди.

Користувач вводить два числа: 
h - кількість годин і m - кількість хвилин.

Підключіть модуль my_time з попереднього завдання,
використовуйте функції переведення часу в секунди.

Виведіть витрачений час в секундах.
'''

# main_program.py

from my_time import seconds_in_hour, seconds_in_min

h = int(input("Введіть кількість годин: "))
m = int(input("Введіть кількість хвилин: "))

total_seconds = seconds_in_hour(h) + seconds_in_min(m)

print(f"Витрачений час в секундах: {total_seconds}")
# my_time.py

# Функція для переведення хвилин у секунди
# Вхідні параметри: m - кількість секунд
# Повернене значення: кількість секунд у хвилинах
def seconds_in_min(m):
    return m * 60

# Функція для переведення годин у секунди
# Вхідні параметри: h - кількість годин
# Повернене значення: кількість секунд у годинах
def seconds_in_hour(h):
    return h * 3600
