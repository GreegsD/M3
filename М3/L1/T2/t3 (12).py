'''
Бути вічливими це так чудово! 
Давайте протестуємо вічливізатор нового покоління!
У програмі написана функція - вічливізатор, яка повертає рядок ", будь ласка". 
Використовуйте цю функцію і напишіть програму, яка отримує від користувача рядок, 
потім за допомогою функції до цього рядка додає ", будь ласка" і виводить результат на екран!
'''
def vvichlyvizator(s):
    return s + ", будь ласка"

# Користувач вводить рядок
user_input = input("Введіть рядок: ")

# Викликаємо функцію та виводимо результат на екран
result = vvichlyvizator(user_input)
print(result)


