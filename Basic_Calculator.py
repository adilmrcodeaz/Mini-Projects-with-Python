"""
Basic Calculator in Python
---------------------------
This program is a command-line calculator that supports basic arithmetic operations:
- Addition
- Subtraction
- Multiplication
- Division

How to Use:
1. Run the program in a Python environment.
2. Select an operation (A, B, C, D) when prompted.
3. Enter two numbers to calculate the result.
4. Enter 'E' to exit.

Author: Adil Rahimov
Date: 25.12.2024
"""

def add(a,b):
    answer = a+b
    print(str(a)+ " + " + str(b)+ " = " + str(answer))


def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mul(a,b):
    answer = a*b
    print(str(a)+ " * "+ str(b)+ " = " + str(answer))

def div(a,b):
    try:
        if b == 0:
            print("Error: Cannot divide by zero!")
            return
        answer = a/b
        print(str(a)+" / "+str(b)+ " = " + str(answer))
    except Exception as e:
        print(f"An error occurred: {e}")

def get_numbers():
    try:
        a = float(input("Please input first number: "))
        b = float(input("Please input second number: "))
        return a, b
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

while True:
    print("\nCalculator Menu:")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Please input your choice: ").upper()

    if choice == 'E':
        print("Program ended")
        break

    if choice not in ['A', 'B', 'C', 'D']:
        print("Error: Please input correct operation (A/B/C/D/E)")
        continue

    a, b = get_numbers()
    if a is None:  # If input was invalid
        continue

    if choice == 'A':
        add(a,b)
    elif choice == 'B':
        sub(a,b)
    elif choice == 'C':
        mul(a,b)
    elif choice == 'D':
        div(a,b)
