#Empty dictionary
user_profile = {}

#asking the user to enter their first name
first_name = str(input("Enter your first name "))
#put the first name in the empty dictionary
user_profile["first name"] = first_name
#asking the user to enter their last name
last_name = str(input("Enter yout last name "))
#put the user last name in the empty dictionary
user_profile["last name"] = last_name
#asking the user to put their username
username = input("Enter your username ")
#put the username in the empty dictionary
user_profile["username"] = username
#asking the user to enter their password
password = input("What is your passsword?" )
#put the password in the empty dictonary
user_profile["password"] = password
#asking the user to put their date of birth
date_of_birth = input("Enter your date of birth (MM/DD/YYYY) ")
#put the date of birth in the empty dictionary
user_profile["date of birth"] = date_of_birth
#asking the user to ad their phone number
telephone = int(input("Enter your phone number "))
#put the username in the empty dictionary
user_profile["telephone"] = telephone

#new key value
user_profile["active_account"] = True

#print the first name
print("First name :",user_profile["first name"])
#print the last name
print("Last name: ", user_profile["last name"])
#print the username
print("username: ",username[username])
#print password
print("password: ",user_profile["password"])
#print date of birth
print("Date of Birth: ",user_profile["date of birth"])
#print the phone number
print("Phone number:",user_profile["telephone"])

#ask if the user wants to login
user_anwer = input("Do you want to attempt login")
if user_anwer.lower() == "yes": #make sure that the user said yes regardless of how he write the yes it's going to work
    print("")
#input()
#max_attempts = 3
for attempt in range (3): #loop for only 3 attempts
    username_input = input("Enter Username")
    password_input = input("Enter password")
    if (username_input == user_profile["username"] and password_input == user_profile["password"]): #check that both username and password match
        if user_profile["active_account"]:  #check if the account is active
            print("You're logged in",user_profile["first name"]) #if it is active print this
            break #stop the loop
        else:
            print("Username or password failed")
            if attempt == 2: #if it's the last attempt print this
                print("You have locked your account. Closing script")
            else:
                print("") #just here for nothing
