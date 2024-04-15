#list of all the variables that we need
Month=["January","February","March","April","May","June","July","August","September","October","November","December"]
Week=[1,2,3,4]
Color=["Red","Brown","Purple","Black"]
#Variable for all the correct answers
RightMonth= Month[0] #January
RightWeek= Week[2]   #third week
RightColor= Color[2] #Purple
#First question: 
guessmonth=input("Please select a month ")
print(guessmonth)
#To check if the month is right
if guessmonth== RightMonth:
    print('That is right')
#Second question:
    guessweek=input("Guess the week of the month ")
#Convert the string to an integer because orginally it'll be a string
    try:
        guessweek= int(guessweek)
#in case the user don't put a number so that you can let them know that it's invalid
    except ValueError: 
        print("You enter a unvalid character please use a number")
        guessweek= None
#to see if the week is right
if guessweek== RightWeek:
    print('That is the right week')
#third question
    guesscolor=input("Select the correct color ")
    if guesscolor== RightColor:
            print("That's the right color")
            if RightMonth:
                if RightWeek:
                    if RightColor:
                        print('You win the game')
else:
    print('Please try again')
