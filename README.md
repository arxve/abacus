 # Terminal-based Python Calculator

This calculator program allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers. It also includes error handling to prevent division by zero.

## How to Use the Calculator

1. Run the `calculator.py` file.
2. Select the operation you want to perform by entering the corresponding number (1 for addition, 2 for subtraction, 3 for multiplication, or 4 for division).
3. Enter the first number.
4. Enter the second number.
5. The result of the operation will be displayed.

## Code Explanation

The calculator program is implemented using the following functions:

* `add(x, y)`: This function adds two numbers and returns the result.
* `subtract(x, y)`: This function subtracts two numbers and returns the result.
* `multiply(x, y)`: This function multiplies two numbers and returns the result.
* `divide(x, y)`: This function divides two numbers and returns the result. If the second number is zero, it returns an error message instead.

The program first prompts the user to select an operation. It then prompts the user to enter the two numbers. Finally, it calls the appropriate function to perform the operation and displays the result.

## Error Handling

The calculator program includes error handling to prevent division by zero. If the user enters zero as the second number for the division operation, the program will display an error message instead of crashing.
