# AI Review: The function name for subtraction is misspelled as 'subtrcat'. It should be 'subtract' to match the operator handling in the main function.
def add(a, b):
    return a + b

def subtrcat(a, b):
    return a - b
    
# AI Review: The multiplication operation is missing. Implement a multiply function.
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
        elif operator == '-':
            result = subtract(num1, num2)
        # AI Review: The multiplication operation is not handled. Add a condition for the '*' operator.
        elif operator == '/':
            result = divide(num1, num2)
       
        else:
            print("⚠️ Invalid operator. Use +, -, *, or /.\n")
            continue

        print(f"Result: {result}\n")

# Progress Analysis:
# - Addition: 100%
# - Subtraction: 0% (function name misspelled)
# - Multiplication: 0% (missing implementation)
# - Division: 100%
# Overall progress: 50%