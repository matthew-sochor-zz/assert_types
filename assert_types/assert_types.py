import inspect
from contextlib import wraps
from typing import Union, List, Dict, Tuple, Iterator
import numpy as np


def assert_types(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        signature = inspect.signature(function)
        parameters = signature.parameters
        keys = parameters.keys()
        for arg, key in zip(args, keys):
            if parameters[key].annotation != inspect._empty:
                assert check_arg(arg, parameters[key].annotation), 'Argument {} is type {} but should be type {}'.format(key, type(arg), parameters[key].annotation)

        for key in kwargs.keys():
            if parameters[key].annotation != inspect._empty:
                assert check_arg(kwargs[key], parameters[key].annotation), 'Key word argument {} is type {} but should be type {}'.format(key, type(kwargs[key]), parameters[key].annotation)
        out = function(*args, **kwargs)
        if signature.return_annotation != inspect._empty:
            if signature.return_annotation is None:
                assert out is None, 'Return type {} should be None'.format(type(out))
            else:
                assert check_arg(out, signature.return_annotation), 'Return type {} should be type {}'.format(type(out), signature.return_annotation)
        return out
    return wrapper


def check_arg(arg, t):
    if hasattr(t, '__origin__'):
        if t.__origin__ is None:
            # There are no sub-args, check against this base type
            return isinstance(arg, t)
        else:
            if t.__args__ is not None:
                if t.__origin__ == Union:
                    return any([check_arg(arg, inner_type) for inner_type in t.__args__])
                elif t.__origin__ == Tuple:
                    if isinstance(arg, t.__origin__):
                        if len(arg) == len(t.__args__):
                            return all([check_arg(inner_arg, inner_type) for inner_arg, inner_type in zip(arg, t.__args__)])
                        else:
                            return False
                    else:
                        return False
                elif t.__origin__ == List:
                    if isinstance(arg, t.__origin__):
                        if len(arg) == 0:
                            return isinstance(arg, t.__origin__)
                        else:
                            # sample 5 random list objects
                            return all([check_arg(arg[i], t.__args__[0]) for i in np.random.randint(0, len(arg), size=5)])
                    else:
                        return False
                elif t.__origin__ == Iterator:
                    return isinstance(arg, t.__origin__)
                elif t.__origin__ == Dict:
                    if isinstance(arg, t.__origin__):
                        return check_arg(arg.keys()[0], t.__args__[0]) and check_arg(arg[arg.keys()[0]], t.__args__[1])
                    else:
                        return False
                else:
                    return isinstance(arg, t.__origin__)
            else:
                return isinstance(arg, t.__origin__)
    else:
        return isinstance(arg, t)
