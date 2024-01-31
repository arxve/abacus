import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def exponentiation(x, y):
    return x ** y

def square_root(x):
    if x < 0:
        return "Cannot calculate square root of a negative number!"
    else:
        return math.sqrt(x)

def factorial(x):
    if x < 0:
        return "Cannot calculate factorial of a negative number!"
    elif x == 0:
        return 1
    else:
        return x * factorial(x-1)

def modulus(x, y):
    if y == 0:
        return "Cannot calculate modulus with zero!"
    else:
        return x % y

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def natural_logarithm(x):
    if x <= 0:
        return "Cannot calculate natural logarithm of non-positive numbers!"
    else:
        return math.log(x)

def base_10_logarithm(x):
    if x <= 0:
        return "Cannot calculate base 10 logarithm of non-positive numbers!"
    else:
        return math.log10(x)

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Square Root")
print("7. Factorial")
print("8. Modulus")
print("9. Sine")
print("10. Cosine")
print("11. Tangent")
print("12. Natural Logarithm")
print("13. Base 10 Logarithm")

while True:
    choice = input("Enter choice (1-13): ")

    if choice in ('1', '2', '3', '4', '8'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '8':
            print("Result:", modulus(num1, num2))
    elif choice in ('5', '6', '7', '9', '10', '11', '12', '13'):
        num = float(input("Enter a number: "))

        if choice == '5':
            exp = float(input("Enter the exponent: "))
            print("Result:", exponentiation(num, exp))
        elif choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", factorial(int(num)))
        elif choice == '9':
            print("Result:", sine(num))
        elif choice == '10':
            print("Result:", cosine(num))
        elif choice == '11':
            print("Result:", tangent(num))
        elif choice == '12':
            print("Result:", natural_logarithm(num))
        elif choice == '13':
            print("Result:", base_10_logarithm(num))
    else:
        print("Invalid Input")
