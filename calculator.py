def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    
    while should_accumulate:
        for symbol in operators:
            print(symbol)
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        
        if operation_symbol in operators:
            answer = operators[operation_symbol](num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {answer}")
        else:
            print("Invalid operation. Please try again.")
            continue
        
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ")
        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)

calculator()