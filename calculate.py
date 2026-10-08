def calculate(operation, a, b, c):

    if operation == 'add':
        return a + b + c
    elif operation == 'subtract':
        return a - b - c
    elif operation == 'multiply':
        return a * b * c
    elif operation == 'divide':
        try:
            return a / b / c
        except ZeroDivisionError:
            return "Error: Divide by Zero Error"
    elif operation == 'exponent':
        return a **b ** c
    else:
        return "Error: Unsupported operation"

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3, 2))        # Output: 8
    print(calculate('subtract', 5, 3, 2))   # Output: 2
    print(calculate('multiply', 5, 3, 2))   # Output: 15
    print(calculate('divide', 5, 3, 2))     # Output: 1.666...
    print(calculate('divide', 5, 0, 3))     # Error: Divide by Zero Error
    print(calculate('exponent',2,2, 2))     # Output: 125