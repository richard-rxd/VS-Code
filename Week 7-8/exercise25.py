def numbcheck(func):
    def negint(*args):
        if args[0] < 0 or args[0] % 1 != 0:
            raise ValueError("Input must be non-negative integer.")
        return func(*args)

    return negint
    
@numbcheck
def factorial(x):
    if x == 0:
        return 1
    if x == 1:
        return 1
    return x * factorial(x-1)

if __name__ == "__main__":
    try:
        print(factorial(1.5))
    except ValueError as e:
        print(e)