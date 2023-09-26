def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Arguments must be integers.")
        return func(*args, **kwargs)
    return wrapper

@validate_input
def add_numbers(a, b):
    return a * b

try:
    print(add_numbers(3, "f"))
except ValueError:
    print("Error")