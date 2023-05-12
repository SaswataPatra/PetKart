def dummy_decorator(func):
    def wrapper(*args, **kwargs):
        print("This is a dummy decorator function")
        return func(*args, **kwargs)
    return wrapper
