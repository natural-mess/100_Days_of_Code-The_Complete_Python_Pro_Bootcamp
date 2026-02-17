# Ex1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)

# Ex2
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num%2==0]
print(result)

# Ex3
with open("file1.txt", mode="r") as file1, open("file2.txt", mode="r") as file2:
    f1_content = [int(line.strip()) for line in file1]
    f2_content = [int(line.strip()) for line in file2]

result = [num for num in f1_content if num in f2_content]

print(result)

