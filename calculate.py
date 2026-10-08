def calculate(operation, a, b):
    output = f'{operation} of {a} and {b} ='
    try: 
        a = int(a)
        b = int(b)
    except:
        return "Error: Not a Number"
    if operation == 'add':
        value = a + b 
        output += f' {value}'
        return output
    elif operation == 'subtract':
        value = a - b 
        output += f' {value}'
        return output
    elif operation == 'multiply':
        value = a * b 
        output += f' {value}'
        return output
    elif operation == 'divide':
        try:
            value = a / b 
            output += f' {value}'
            return output
        except ZeroDivisionError:
            return "Error: Divide by Zero Error"
    elif operation == 'exponent':
        value = a **b 
        output += f' {value}'
        return output
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