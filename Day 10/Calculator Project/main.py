import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(calculator["*"](4,8))

while True:
    print(art.logo)

    first_num = float(input("What's the first number?: "))

    continue_calculation = "y"

    while continue_calculation == "y":
        for key in calculator:
            print(key)

        operation = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))

        result = calculator[operation](first_num, next_num)
        print(f"{first_num} {operation} {next_num} = {result}")

        continue_calculation = input(f"Type \'y\' to continue calculating with {result}, or type \'n\' to start a new calculation: ")
        if continue_calculation == "y":
            first_num = result
            print("\n * 20")

