import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# rand_num_0_to_1 = random.random()
# print(rand_num_0_to_1)

# random_float = random.uniform(1, 10)
# print(random_float)

random_coin = random.randint(1, 2)
if random_coin == 1:
    print("Heads")
else:
    print("Tails")