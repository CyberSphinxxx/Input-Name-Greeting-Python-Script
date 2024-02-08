name = input("Enter Your Name: ") #promts user to enter name,

while len(name) == 0: #checks the name variable if theres anything inside it
    name = input("No name entered, please enter your name: ") #if no named entered

print(f"Hello {name} welcome!") #the code proceeds here if name is more than 0 char
