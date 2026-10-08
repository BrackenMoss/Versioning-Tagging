def calculate(operation, a, b):
    try: 
        a = int(a)
        b = int(b)
    except:
        return "Error: Not a Number"
    if operation == 'add':
        return a + b 
    elif operation == 'subtract':
        return a - b 
    elif operation == 'multiply':
        return a * b 
    elif operation == 'divide':
        try:
            return a / b 
        except ZeroDivisionError:
            return "Error: Divide by Zero Error"
    elif operation == 'exponent':
        return a **b 
    else:
        return "Error: Unsupported operation"
    

# Example usage
if __name__ == "__main__":
    print(calculate('add', 5, 3))        # Output: 8
    print(calculate('subtract', 5, 3))   # Output: 2
    print(calculate('multiply', 5, 3))   # Output: 15
    print(calculate('divide', 5, 3))     # Output: 1.666...
    print(calculate('divide', 5, 0))     # Error: Divide by Zero Error
    print(calculate('exponent',2,2))     # Output: 125
    print(calculate('add','five','three'))