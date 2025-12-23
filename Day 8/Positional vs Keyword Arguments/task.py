# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Rocky", "Nowhere")
greet_with(location="London", name="Angela")

def calculate_love_score(name1, name2):
    true = "true"
    love = "love"
    name = (name1+name2).lower()
    countTrue = 0
    countLove = 0
    for letter in true:
        countTrue += name.count(letter)
    for letter in love:
        countLove += name.count(letter)
    print(f"{countTrue}{countLove}")