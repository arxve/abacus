import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def exponentiate(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number!")
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Cannot calculate factorial of a negative number!")
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

def modulus(x, y):
    if y == 0:
        raise ValueError("Cannot calculate modulus with zero!")
    return x % y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def natural_logarithm(x):
    if x <= 0:
        raise ValueError("Cannot calculate natural logarithm of non-positive numbers!")
    return math.log(x)

def base_10_logarithm(x):
    if x <= 0:
        raise ValueError("Cannot calculate base 10 logarithm of non-positive numbers!")
    return math.log10(x)

OPERATIONS = {
    '1': ("Addition", add),
    '2': ("Subtraction", subtract),
    '3': ("Multiplication", multiply),
    '4': ("Division", divide),
    '5': ("Exponentiation", exponentiate),
    '6': ("Square Root", square_root),
    '7': ("Factorial", factorial),
    '8': ("Modulus", modulus),
    '9': ("Sine", sine),
    '10': ("Cosine", cosine),
    '11': ("Tangent", tangent),
    '12': ("Natural Logarithm", natural_logarithm),
    '13': ("Base 10 Logarithm", base_10_logarithm),
    'q': ("Quit", None),
}

def get_valid_operation():
    while True:
        print("\nSelect operation:")
        for key, value in OPERATIONS.items():
            print(f"{key}. {value[0]}")
        choice = input("Enter choice (1-13, q to quit): ").strip().lower()
        if choice in OPERATIONS:
            return OPERATIONS[choice][1]
        else:
            print("Invalid choice. Please try again.")

def get_valid_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    while True:
        operation = get_valid_operation()
        if operation is None:
            print("Exiting calculator. Goodbye!")
            break
        elif operation in (add, subtract, multiply, divide, modulus):
            num1 = get_valid_number("Enter first number: ")
            num2 = get_valid_number("Enter second number: ")
            try:
                result = operation(num1, num2)
                print("Result:", result)
            except ValueError as ve:
                print("Error:", ve)
        else:
            num = get_valid_number("Enter a number: ")
            try:
                result = operation(num)
                print("Result:", result)
            except ValueError as ve:
                print("Error:", ve)

if __name__ == "__main__":
    main()
