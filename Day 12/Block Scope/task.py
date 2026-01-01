game_level = 10
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    new_enemy = ""
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    count = 0
    for i in range(2, num):
        if num % i == 0:
            return False

    return True
