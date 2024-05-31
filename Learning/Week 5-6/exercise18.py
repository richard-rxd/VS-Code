# Task 1
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    summ = arr[-1] + sum(arr[0:-1])
    return summ

print(sum([3,4,6,2,25,52,52,8]))
print(sum([2, 4, 5, 6, 7]))

# Task 2
# Define a function named to_string that converts a number 'n' to a string representation
# in a given 'base' using a character set "0123456789ABCDEF"
def to_string(n, base):
    # Define a character set for the conversion in hexadecimal format
    conver_tString = "0123456789ABCDEF"
    
    # Check if the number 'n' is less than the specified base
    if n < base:
        # If 'n' is less than the base, return the corresponding character from the character set
        return conver_tString[n]
    else:
        # If 'n' is greater than or equal to the base, recursively call the to_string function
        # to convert the quotient (n // base) to a string and concatenate it with the remainder
        # (n % base) represented in the character set
        return to_string(n // base, base) + conver_tString[n % base]

# Print the result of calling the to_string function with the input values 2835 and 16
print(to_string(2835, 16))

# Task 3
def sum(arr):
    total = 0
    for element in arr:
        if type(element) == type([]):
            total = total + sum(element)
        else: 
            total = total + element
    return total

print(sum([1, 2, [3,4], [5,6]]))

# Task 4
def factorial(number):
    if number == 1:
        return number
    return number * factorial(number-1) 

print(factorial(7))

# Task 5
def fibonacci(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(10))

# Task 6
def sumDigits(n):
    # Check if 'n' is 0 (base case for summing digits)
    if n == 0:
        # If 'n' is 0, return 0 (no digits to sum)
        return 0
    else:
        # If 'n' is not 0, calculate the sum of the last digit (n % 10) and
        # recursively call the sumDigits function on the remaining digits (n / 10)
        return n % 10 + sumDigits(int(n / 10))

print(sumDigits(345))

# Task 7
def sumpositive(number):
    if number % 2 != 0:
        return "Invalid input"
    if number == 0:
        return 0
    return number + sumpositive(number-2)

print(sumpositive(6))

# Task 8
def harmonicseries(number):
    if number == 1:
        return 1
    return 1/number + harmonicseries(number - 1)

print(harmonicseries(7))

# Task 9
"""def geometricseries(a, q, n):
    if n == 1:
        return a + a*q
    return a*q**n + geometricseries(a,q,n-1)

print(geometricseries(1,2,3))"""

# Define a function named geometric_sum that calculates the geometric sum up to 'n' terms
def geometric_sum(n):
    # Check if 'n' equals 0, which is the base case for the geometric sum
    if n == 0:  # Corrected base case condition
        # If 'n' equals 0, return 1 as the geometric sum in this case is 1
        return 1
    else:
        # If 'n' is not 0, calculate the term in the geometric series (1 / 2^n) and add it to
        # the result of recursively calling the geometric_sum function with 'n - 1'
        return 1 / (pow(2, n)) + geometric_sum(n - 1)
# Print the result of calling the geometric_sum function with the input value 7
print(geometric_sum(7))

# Task 10
def power(a,b):
    if a == 0:
        return 0
    if b == 0:
        return 1
    if b == 1:
        return a
    return a * power(a,b-1)

print(power(3,4))

# Task 11
def gcd(a, b, divider = 1):
    min_n = min(a, b)
    for i in range(divider+1, min_n+1):
        if a % i == 0 and b % i == 0:
            return gcd(a, b, i)
    return divider
    
print(gcd(169, 13))

def Recurgcd(a, b):
    # Determine the lower and higher values between 'a' and 'b'
    low = min(a, b)
    high = max(a, b)

    # Check if the lower value is 0 (base case for GCD calculation)
    if low == 0:
        # If the lower value is 0, return the higher value (GCD is the non-zero value)
        return high
    # Check if the lower value is 1 (base case for GCD calculation)
    elif low == 1:
        # If the lower value is 1, return 1 (GCD of any number with 1 is 1)
        return 1
    else:
        # If neither base case is met, recursively call the Recurgcd function
        # with the lower value and the remainder of the higher value divided by the lower value
        return Recurgcd(low, high % low)

# Print the result of calling the Recurgcd function with the input values 12 and 14
print(Recurgcd(54, 30))