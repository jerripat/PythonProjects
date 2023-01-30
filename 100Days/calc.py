from replit import clear


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    raise n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    num1 = int(input("Whats the first number?:"))

    for symbol in operations:
        print(symbol)
        if symbol == "x":
            print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operstion : ")
        num2 = int(input("Whats the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if (input(f"Type 'y' to continue: with {answer}, or type 'n' to start new: ") == "y" ):
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
