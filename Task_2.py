#Задача 2. Напишите программу, которая принимает от пользователя число в диапазоне 1-99 и возвращает его прописью
string = input('Введите целое число или ряд целых чисел для перевода (от 1 до 99): ')

a = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
     6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
b = {10: 'десять', 20: 'двадцать', 30: 'тридцать', 40: 'сорок',
     50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
     80: 'восемьдесят', 90: 'девяносто'}
c = {11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать',
     14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
     17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

number_list = string.replace(',', '').split()

for i in number_list:
    i = [int(num) for num in filter(lambda num: num.isnumeric(), number_list)]
    break
for number in i:
    number1 = number % 10
    number2 = number - number1
    for j in range(number):
        if number < 10:
            print(f'Вы ввели: {number}, это число прописью: {a.get(number).capitalize()}')
            break
        elif 10 < number < 20:
            print(f'Вы ввели: {number}, это число прописью: {c.get(number).capitalize()}')
            break
        elif number >= 10 and number in b:
            print(f'Вы ввели: {number}, это число прописью: {b.get(number).capitalize()}')
            break
        elif number >= 100:
            print(f'Число {number} не находится в диапазоне 1-99')
            break
        else:
            print(f"Вы ввели: {number}, ваше число прописью: {(b.get(number2) + ' ' + a.get(number1)).capitalize()}")
            break