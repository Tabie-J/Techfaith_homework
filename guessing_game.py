import random 
def guessing_game():
    print("Hello, Hello :) \n")
    print("Welcome to THE Guessing game ")
    print("Guess a number between 60 and 100")
    print("You have only 5 attemps. I know you can do it")

    number = random.randint(60 , 100)
    attempts = 5

    while attempts>0:
        user_guess = int(input("Enter your guess: \n"))
        if user_guess <60 or user_guess >100:
            print("Not in range, try again")
            continue
        if user_guess == number:
            print("You got it right I knew you can do it")
            break
        if user_guess > number:
            print("Too high, try again ")
        else:
            print("Too low try again")
            
            attempts -=1
            print("You have",attempts,"attempts left \n")
            if attempts == 0:
                print("You've reached your final attempts. The number was",number)
                print("Better luck next time! Thanks for playing ;) ")
                
guessing_game()
