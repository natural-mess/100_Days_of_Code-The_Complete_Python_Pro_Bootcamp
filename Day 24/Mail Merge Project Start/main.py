#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Letters/starting_letter.txt") as starting_letter:
    starting_letter_content = starting_letter.read()
    with open("./input/Names/invited_names.txt") as invited_names:
        list_of_names = invited_names.readlines()
        for name in list_of_names:
            new_name = name.strip()
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as new_letter:
                new_letter_content = starting_letter_content.replace("[name]", new_name)
                new_letter.write(new_letter_content)
