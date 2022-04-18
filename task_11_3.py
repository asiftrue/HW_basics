class MyErr(Exception):
    pass


num = None
a = []
while num != 'stop':
    try:
        num = input('Введите число или введите stop для завершения и вывода списка: ')
        if num == 'stop':
            print(a)
            break
        else:
            if num.isdigit():
                a.append(num)
            else:
                raise MyErr('Введено не число, необходмо вводить только числа.')

    except MyErr as err:
        print(err)
