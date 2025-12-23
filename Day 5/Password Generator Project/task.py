import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)

# create a list from string, then shuffle the list, then join the characters to recreate string
char_list = list(password)
random.shuffle(char_list)
print(''.join(char_list))

# Method 2
# random.choices returns multiple random elements from the list with replacement
rand_letters = random.choices(letters, k=nr_letters)
rand_numbers = random.choices(numbers, k=nr_numbers)
rand_symbols = random.choices(symbols, k=nr_symbols)
password2 = rand_letters + rand_numbers + rand_symbols

# random.sample returns a particular length list of items chosen from the sequence i.e. list, tuple, string or set.
# Used for random sampling without replacement.
randomized_password = random.sample(password2, k=len(password2))
print(''.join(randomized_password))
