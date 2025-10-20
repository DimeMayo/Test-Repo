# Missing subtraction function
# AI Review: The code does not include a subtraction function, which is required for the calculator. 
# To fix this, implement a function called `subtract(a, b)` that returns `a - b`.

def add(a, b):
    return a + b

# Missing subtraction function
# AI Review: The code does not include a subtraction function, which is required for the calculator. 
# To fix this, implement a function called `subtract(a, b)` that returns `a - b`.

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("🧮 Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        num1 = input("Enter the first number (or 'q' to quit): ")
        
        if num1.lower() == 'q':
            print("Goodbye!")
            break
        
        num2 = input("Enter the second number: ")
        operator = input("Enter an operator (+, -, *, /): ")

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid number. Try again.\n")
            continue

        if operator == '+':
            result = add(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            # AI Review: Division by zero can cause a runtime error. 
            # To fix this, check if num2 is zero before performing the division.
            result = divide(num1, num2)
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress: 50% (add and subtract functions are missing, division by zero check is needed)