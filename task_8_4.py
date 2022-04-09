from functools import wraps


def val_checker(callback):
    def val_check(func):
        @wraps(func)
        def wrapper(*args):
            for ar in args:
                if not callback(ar):
                    raise ValueError(f'wrong val {ar}')
            cube = func(*args)
            return cube

        return wrapper

    return val_check


@val_checker(lambda x: x > 0)
def calc_cube(x):
    '''Some message about calc_cube'''
    return x ** 3


a = calc_cube(-5)
print(a)
# help(calc_cube)
