def uppercase_generator(func):
    def wrapper(*args):
        for value in func(*args):
            yield str(value).upper()
    return wrapper

@uppercase_generator
def generator():
    yield "python"
    yield "c++"
    yield "c#"

for pr in generator():
    print(pr)

