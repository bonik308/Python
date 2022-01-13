def ex_decorator(func):
    def wrapper(*args, **kwargs):
        for i in args:
            print(f'{str(func).split()[1]}({i}: {type(i)})')
        for i in kwargs:
            print(f'{str(func).split()[1]}([ARG: {i}] = {kwargs[i]}: {type(kwargs[i])})')
        return func(*args, **kwargs)
    return wrapper

@ex_decorator
def function_with_arguments(a, b, c, d):
    try:
        b = int(b)
        b = b ** 3
    except:
        b = 0
    return b

print(f'Результат функции, обернутой декоратором: {function_with_arguments(a="TEXT", b=2, c=555, d={1: "2"})}')