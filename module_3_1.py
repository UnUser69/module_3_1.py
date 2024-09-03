'''Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
Давайте реализуем данную фишку самостоятельно!

Вам необходимо написать 3 функции:
Функция count_calls подсчитывающая вызовы остальных функций.
Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
Пункты задачи:
Создать переменную calls = 0 вне функций.
Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
Создать функцию string_info с параметром string и реализовать логику работы по описанию.
Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
Вывести значение переменной calls на экран(в консоль).'''

import random
from pyloremgen.generator.lorem_text import LoremIpsum

lorem_generator = LoremIpsum()

calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return length, upper, lower

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    list_to_search = [item.lower() for item in list_to_search]
    return string in list_to_search

# Generate random strings and lists to test the functions
for _ in range(random.randint(1, 10)):
    string = lorem_generator.words(words_numbers=1)
    print(string_info(string))

for _ in range(random.randint(1, 10)):
    string = lorem_generator.words(words_numbers=1)
    list_to_search = lorem_generator.paragraphs(paragraphs_numbers=1, size="medium", start_with_lorem_ipsum=True).split()
    print(is_contains(string, list_to_search))

print(f"Total calls: {calls}")
