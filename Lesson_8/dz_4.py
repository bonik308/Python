def ex_decorator(f):
    def _ex_decorator(func):
        def wrapper(*args):
            l1 = set(args)
            l2 = set(filter(f, args))
            for i in l2:
                for i in l1 - l2:
                    raise ValueError(f'wrong val {i}')
                return func(i)
        return wrapper
    return _ex_decorator

@ex_decorator(lambda x: x > 0)
def calc_cube(b):
    return b ** 3

print(calc_cube(6))