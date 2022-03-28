# Задача 5-1, с yield
def my_num_gen(n):
    for number in range(1,n + 1, 2):
        yield number
print(*my_num_gen(25))

# Задача 5-2, без yield
m = 25
numbers = (number for number in range(1, m + 1, 2))
print(*numbers)
