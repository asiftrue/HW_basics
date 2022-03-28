from time import perf_counter

# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]

# через множества
start = perf_counter()
unique_src = set()
rep_src = set()
for num in src:
    if num in rep_src:
        continue
    if num in unique_src:
        unique_src.discard(num)
        rep_src.add(num)
        continue
    unique_src.add(num)
# print(unique_src) #все перемешано
print([num for num in src if num in unique_src])  # в том же порядке, как в исходном списке
print('Через множества: ', perf_counter() - start)

# через словарь
start = perf_counter()
my_dict = {}
for num in src:
    if num in my_dict:
        my_dict[num] += 1
    else:
        my_dict[num] = 1

print([el for el in src if my_dict[el] == 1])
print('Через словарь: ', perf_counter() - start)

# так делать не надо, O(n) * O(n) -> O(n ** 2)
# start = perf_counter()
# for num in src:
#     if src.count(num) == 1:
#         print(num)
# print('Через count: ', perf_counter() - start)
