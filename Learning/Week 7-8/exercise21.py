def square():
    num = 1
    while True:
        yield num**2
        num += 1

for res in square():
    if res > 101:
        break
    print(res)