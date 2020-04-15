# задача: Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
n = input('Введите число n: ')
result_a = n + n
result_b = n + n + n
print('Сумма чисел n + nn + nnn: ' + str(int(n) + int(result_a) + int(result_b)))