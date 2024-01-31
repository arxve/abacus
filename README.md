 # Terminal-based Python Calculator

This is a simple calculator that can perform various mathematical operations. It is written in Python and uses a menu-driven interface to allow the user to select the operation they want to perform.

## How to Use

To use the calculator, simply run the `calculator.py` file. You will be presented with a menu of options. Select the operation you wish to perform by entering the corresponding number.

If the operation requires two numbers, you will be prompted to enter them. Otherwise, you will only need to enter one number.

The result of the operation will be printed to the console.

## Options

The following operations are available:

* Addition (+)
* Subtraction (-)
* Multiplication (*)
* Division (/)
* Exponentiation (^)
* Square root (√)
* Factorial (!)
* Modulus (%)
* Sine (sin)
* Cosine (cos)
* Tangent (tan)
* Natural logarithm (ln)
* Base 10 logarithm (log)

## Example

Here is an example of how to use the calculator:

```
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exponent
6. Square Root
7. Factorial
8. Modulus
9. Sine
10. Cosine
11. Tangent
12. Natural Logarithm
13. Base 10 Logarithm

Enter choice (1-13): 1
Enter first number: 10
Enter second number: 5
Result: 15.0
```

## Code Explanation

The calculator program is implemented using the following functions:

* `add(x, y)`: This function adds two numbers and returns the result.
* `subtract(x, y)`: This function subtracts two numbers and returns the result.
* `multiply(x, y)`: This function multiplies two numbers and returns the result.
* `divide(x, y)`: This function divides two numbers and returns the result. If the second number is zero, it returns an error message instead.
* `exponentiation(x, y)`: This function takes two arguments, x and y and returns x raised to the power of y. 
* `square_root(x)`: This function takes one argument, x, and returns the square root of x. If x is negative, it returns an error message.
* `factorial(x)`: This function takes one argument, x, and returns the factorial of x. If x is negative, it returns an error message. If x is 0, it returns 1.
* `modulus(x, y)`: This function takes two arguments, x and y, and returns the remainder of x divided by y. If y is 0, it returns an error message.
* `sine(x)`: This function takes one argument, x, and returns the sine of x radians. It converts x to radians before calculating the sine.
* `cosine(x)`: This function takes one argument, x, and returns the cosine of x radians. It converts x to radians before calculating the cosine.
* `tangent(x)`: This function takes one argument, x, and returns the tangent of x radians. It converts x to radians before calculating the tangent.
* `natural_logarithm(x):` This function takes a number x as an argument and returns its natural logarithm using the math.log() function.
* `base_10_logarithm(x)`: This function calculates the base 10 logarithm of a positive number x using the math.log10() function.

The program first prompts the user to select an operation. It then prompts the user to enter the two numbers. Finally, it calls the appropriate function to perform the operation and displays the result.

## Error Handling

The calculator program includes error handling to prevent division by zero. If the user enters zero as the second number for the division operation, the program will display an error message instead of crashing.
