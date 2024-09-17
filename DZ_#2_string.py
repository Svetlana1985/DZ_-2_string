# Задание №1
# text = input('Введите текст: ').lower()
# words = input('Введите список слов через пробел: ').lower().split()
# found_words = []
# text_list = text.split()
#
# for word in words:
#     if word in text_list:
#         found_words.append(word)
# print(' '.join(found_words).upper())
import re

# Задание №2
# exp = input('Введите арифметическое выражение, используя "+" "-" "*" "/": ')
# num1 = ''
# num2 = ''
# operator = ''
# for i in exp:
#     if i.isdigit():
#         if operator == '':
#             num1 += i
#         else:
#             num2 += i
#     else:
#         operator = i
#
# num1 = int(num1)
# num2 = int(num2)
#
# if operator == '+':
#     print(num1 + num2)
# elif operator == '-':
#     print(num1 - num2)
# elif operator == '*':
#     print(num1 * num2)
# elif operator == '/':
#     print(num1 / num2)
# else:
#     print('Не корректно введен оператор')

# Задание №3
# string = 'Добродушный'
# print("Исходная строка : " + str(string))
# substring = []
# for i in range(len(string)):
# 	for j in range(i+1, len(string)+1):
# 		substring.append(string[i:j])
#
# print("Все найденные подстроки : " + str(substring))

# if string.isdigit() == 'True':
#
# 	print(count)
#Задание №4
string = 'До#бр&&од1уш3ны5й'
print("Исходная строка : " + str(string))

count_d = sum(1 for i in string if i.isdigit())
count_a =  sum(1 for i in string if i.isalpha())
count_symbol = sum(1 for i in string if i in ('[','^','&','$','#',']'))
print(f'В строке: цифр {count_d} ,букв {count_a} ,символов {count_symbol} ')


