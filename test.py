def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def main():
# ⚠️ Avoid using print() in production code.
    print("🧮 Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        # Get user input
        num1 = input("Enter the first number (or 'q' to quit): ")
        if num1.lower() == 'q':
# ⚠️ Avoid using print() in production code.
            print("Goodbye!")
            break
        num2 = input("Enter the second number: ")
        operator = input("Enter an operator (+, -, *, /): ")

        # Convert input to float
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
# ⚠️ Avoid using print() in production code.
            print("⚠️ Invalid number. Try again.\n")
            continue

        # Perform calculation
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
# ⚠️ Avoid using print() in production code.
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

# ⚠️ Avoid using print() in production code.
        print(f"Result: {result}\n")

if __name__ == "__main__":
    main()