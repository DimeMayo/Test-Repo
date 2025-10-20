# AI Review: The subtraction operation is missing. Implement a `subtract` function and include it in the main logic to handle the '-' operator.
# AI Review: There is no error handling for division by zero in the `divide` function. This can cause a runtime error if the second number is zero.

def add(a, b):
    return a + b

# AI Review: Missing subtraction function
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # AI Review: Division by zero should be handled to avoid runtime errors
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
        # AI Review: Missing case for subtraction
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress: 50% (add, multiply, and divide implemented; subtract and division by zero handling missing)