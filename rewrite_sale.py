from sys import argv

SYMBS = 12 + 2
num1 = int(argv[1])
num2 = argv[2]

with open('bakery.csv', 'r+', encoding='utf-8') as f:
    i = 0
    for line in f:
        i += 1
    if num1 <= i:
        f.seek((num1 - 1) * SYMBS)
        f.write(f'{num2:>12}\n')
    else:
        print('Такой суммы нет')
