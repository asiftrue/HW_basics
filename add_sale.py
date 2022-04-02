import sys

amount = sys.argv[1]

with open('bakery.csv', 'a', encoding='utf-8') as f:
    f.write(f"{amount:>12}\n")
    # print(amount, file=f)

# можно функцию написать
# def write_sale(argv):
#     with open('bakery.csv', 'a', encoding='utf-8') as f:
#         progra, *args = argv
#         for el in args:
#             f.write(f'{el:>12}\n')
#         return 0

