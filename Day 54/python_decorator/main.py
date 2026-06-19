# Functions are first-class objets, can be passed around as arguments
# e.g. int/string/float etc
# def add(n1, n2):
#     return n1+n2

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)

# result = calculate(add, 2, 3)
# print(result)

# Nested functions
# def outer_func():
#     print("I'm outer")

#     def nested_func():
#         print("I'm inner")

#     nested_func()

# outer_func()

# Functions can be returned from other functions
def outer_func():
    print("I'm outer")

    def nested_func():
        print("I'm inner")

    return nested_func
inner_function = outer_func()
inner_function()