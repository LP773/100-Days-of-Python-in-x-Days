import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

addition = add
subtraction = subtract
multiplication = multiply
division = divide

math_operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    print(art.logo)
    input_number = float(input("First Number: "))

    stopLoop = False
    while stopLoop != True:
        for operation in math_operations:
            print(operation)
        selected_op = input("Pick an operation: ")
        input_second_number = float(input("Second Number: "))
        if selected_op == "+":
            result = math_operations["+"](input_number,input_second_number)
            print(f"{input_number} {selected_op} {input_second_number} = {result}")
        elif selected_op == "-":
            print(f"{input_number} {selected_op} {input_second_number} = {subtract(input_number, input_second_number)}")
            result = subtract(input_number, input_second_number)
        elif selected_op == "*":
            print(f"{input_number} {selected_op} {input_second_number} = {multiply(input_number, input_second_number)}")
            result = multiply(input_number, input_second_number)
        else:
            print(f"{input_number} {selected_op} {input_second_number} = {divide(input_number, input_second_number)}")
            result = divide(input_number, input_second_number)
        input_continue = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation? (y/n): ")
        if input_continue == "y":
            input_number = result
        else:
            stopLoop = True
            print("\n" * 20)
            calculator()

calculator()
