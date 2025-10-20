```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # AI Review: It's good to handle division by zero, but consider raising an exception for better error handling.
    if b == 0:
        return "Error: Cannot divide by zero!"
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

        # AI Review: It's better to validate both numbers before trying to convert them to float.
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("⚠️ Invalid number. Try again.\n")
            continue

        # AI Review: Consider using a dictionary to map operators to functions for cleaner code.
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            # AI Review: This message is clear, but consider logging the invalid operator for debugging.
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        # AI Review: Ensure that the result is valid before printing it.
        print(f"Result: {result}\n")


if __name__ == "__main__":
    main()
```