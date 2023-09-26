def repeat(n):
    def decorator(func):
        def wrapper():
            for i in range(n):
                print(func())
        return wrapper
    return decorator


@repeat(3)
def print_hello():
    return "Hello World"

print_hello()