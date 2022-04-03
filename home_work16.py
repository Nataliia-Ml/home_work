# Написать декоратор, который будет анализировать переданные в декорируемую функцию аргументы
# (позиционные и именованные) и в случае если один из аргументов является типом данных list или tuple
# конвертировать его в set

def argument_analysis(func):
    def wrapper(*args, **kwargs):
        args_list = []
        for arg in args:
            if isinstance(arg, (list, tuple)):
                args_list.append(set(arg))
            else:
                args_list.append(arg)
        args_list = tuple(args_list)
        for k, v in kwargs.items():
            if isinstance(v, (list, tuple)):
                kwargs[k] = set(v)
        return func(*args_list, **kwargs)

    return wrapper


if __name__ == '__main__':
    @argument_analysis
    def new_func(*args, **kwargs):
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")


    new_func([1, 1, 2, 3, 3, 4, 5], (10, 20, 30, 30, 40, 40, 50), triplets_list=[3, 33, 333, 333, 333],
             fours_set={4, 4, 444, 444, 44})
