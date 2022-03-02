import art

# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "-" : subtract,
    "+" : add,
    "*" : multiply,
    "/" : divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    
    for operation in operations:
        print(operation)
    should_continue = True
    
    while should_continue :
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_input = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to try a new calculation, or 'x' to exit : ") 
        if user_input == "y":
            num1 = answer
        elif user_input == "n":
            should_continue = False
            calculator()
        else :
            should_continue = False


print(art.logo)
calculator()
