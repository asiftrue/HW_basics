class MyErr(Exception):
    pass


try:

    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    if y == 0:
        raise MyErr('На ноль делить нельзя!')
    a = x / y
except MyErr as e:
    print(e)
else:
    print(round(a, 2))
# finally:
#     print('Конец программы.')
