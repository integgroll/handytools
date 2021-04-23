import copy


def obtuse_demutable(func):
    """
    This decorator is used as a bugfix for functions with mutable values in their default values from the function definition
    This will not save the initial values from the first time it is called, but it will set them to a blank list or dict
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        func.__defaults__ = tuple([[arg, type(arg)()][isinstance(arg, (list, dict))] for arg in func.__defaults__])
        func(*args, **kwargs)

    return wrapper


def demutable(func):
    """
    This decorator is used as a bugfix for functions with mutable values in their default values from the function definition
    This saves the initial values of the function instead of being obtuse and setting them to blank lists or dicts
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        # Save the initial state of the function's default arguments
        default_storage, kwdefault_storage = copy.deepcopy(func.__defaults__), copy.deepcopy(func.__kwdefaults__)
        # 'Run' the Function and store the results in a return value
        ret_func = func(*args, **kwargs)
        # Set the functions arguments back to their default state
        func.__defaults__, func.__kwdefaults__ = default_storage, kwdefault_storage
        return ret_func

    return wrapper
