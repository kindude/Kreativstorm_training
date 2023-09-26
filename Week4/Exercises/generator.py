def numbers(start,stop, step):
    current = start
    while current < stop:
        yield current
        current += step

for num in numbers(10, 31, 5):
    if num % 3 == 0:
        print(num)

