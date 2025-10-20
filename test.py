# Missing requirement: The multiplication operation is not implemented.
# Progress: 75%

def add(a, b):
    return a + b

# AI Review: The function name is misspelled; it should be 'subtract' instead of 'subtrcat'.
def subtrcat(a, b):
    return a - b
    
def divide(a, b):
    return a / b

# AI Review: The multiplication operation is missing. Implement a multiply function.
# AI Review: The function 'subtract' is referenced but not defined; it should be 'subtrcat'.
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
        elif operator == '-':
            # AI Review: The function 'subtract' is referenced but not defined; it should be 'subtrcat'.
            result = subtract(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")