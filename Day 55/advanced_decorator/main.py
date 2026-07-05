# TODO: Create the logging_decorator() function 👇

def logging_decorator(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        print(f"It returned: {func(*args)}")
        return func(*args)

    return wrapper


# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)