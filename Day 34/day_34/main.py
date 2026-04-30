age: int
name: str
height: float
is_human: bool

# Type hints
# -> bool: expect function to return boolean data type
# age: int: expect input parameter to be of type int
def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive

print(police_check(19))