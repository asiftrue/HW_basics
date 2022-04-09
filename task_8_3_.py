from functools import wraps


def type_logger(callback):
    @wraps(callback)
    def wrapper(*args):
        cube = callback(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
            print(f'{cube}, {type(cube)}')
            print(f'{callback.__name__}({args[0]}: {type(args[0])})')
        else:
            for ar in args:
                print(f'{ar}: {type(ar)}')
        return cube

    # #         for i in args:
    # #             print(type(args[i]))
    # #         # calc_cube()
    # #         # for i in args:
    # #         #     print(f'{i}: {type(i)}')
    # #         #     # return cube
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

help(calc_cube)
