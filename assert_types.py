import inspect


def assert_types(function):

    def wrapper(*args, **kwargs):
        signature = inspect.signature(function)
        parameters = signature.parameters
        keys = parameters.keys()
        for arg, key in zip(args, keys):
            if parameters[key].annotation != inspect._empty:
                assert isinstance(arg, parameters[key].annotation), 'Argument {} is type {} but should be type {}'.format(key, type(arg), parameters[key].annotation)

        for key in kwargs.keys():
            if parameters[key].annotation != inspect._empty:
                assert isinstance(kwargs[key], parameters[key].annotation), 'Key word argument {} is type {} but should be type {}'.format(key, type(kwargs[key]), parameters[key].annotation)
        out = function(*args, **kwargs)
        if signature.return_annotation != inspect._empty:
            if signature.return_annotation is None:
                assert out is None, 'Return type {} should be None'.format(type(out))
            else:
                assert isinstance(out, signature.return_annotation), 'Return type {} should be type {}'.format(type(out), signature.return_annotation)
        return out
    return wrapper

