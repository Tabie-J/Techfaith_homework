import random   # lets us pick random characters

# Character lists
lowercase = ['a', 'b', 'c', 'd', 'e', 'f']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F']
symbols   = ['!', '@', '#', '$', '%', '^']

# Get user choices
def user_input():
    print("Choose what characters you want:")
    print("1 - Lowercase only")
    print("2 - Lowercase + Uppercase")
    print("3 - Lowercase + Uppercase + Symbols")

    choice = int(input("Enter 1, 2, or 3: "))
    length = int(input("How long should the password be? "))

    return choice, length

# Make the password
def generate_password(choice, length):

    # pick which lists we will use
    if choice == 1:
        characters = lowercase
    elif choice == 2:
        characters = lowercase + uppercase
    elif choice == 3:
        characters = lowercase + uppercase + symbols

    password = ""   # start with an empty string

    # build the password one character at a time
    for x in range(length):
        random_character = random.choice(characters)   # pick a random character
        password = password + random_character         # add it to the password

    return password

# Run the program
choice, length = user_input()
final_password = generate_password(choice, length)

print("Your password is:", final_password)
