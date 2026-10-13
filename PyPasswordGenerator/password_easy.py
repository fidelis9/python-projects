import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# initialize an empty set
password_set = []

# add random characters  to the set based on what the user enters
for letter in range(0, nr_letters):
    password_set.append(random.choice(letters)) # add each letter chosen to the set
    
for symbol in range(0, nr_symbols):
    password_set.append(random.choice(symbols))

for number in range(0, nr_numbers):
    
    password_set.append(random.choice(numbers))

# next step is to arrange the items in set as a string instead of list items
password = "".join(password_set) # join the items

print(f"Your password is: {password}")