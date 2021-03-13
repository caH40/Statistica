# Описание блока try,except,else,finally
print('Введите число')
try:
    a = float(input())
    procent = 100/a
    print('100/a = %s' % procent)
# При возникновении определенной ошибки можно конкретно её указать, например ZeroDivisionError
except ZeroDivisionError:
    print('Деление на ноль не возможно')
# При возникновении определенной ошибки можно конкретно её указать, например ValueError
except ValueError:
    print('Вы ввели не число')
# expect должен быть в конце, после условных expect
except:
    print('Возникла ошибка')
# Если ошибок не было, то выполнится блок else
else:
    print('Всё выполнилось без ошибок')
# Блок finally выполняется в любом случае
finally:
    print('Блок выполняется в любом случае')