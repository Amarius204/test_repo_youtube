import random

top_number = input("Type a number for the ceiling: ") #created our first variable for our game
# This variable will allow the user to input a number for our cieling range

if top_number.isdigit():
    top_number = int(top_number) #converts the users string input number into a integer

    if top_number <= 0:
        print("The number must be greater than 0")
        quit() #if the number the user entered for the first variable is not greater than 0, the program will quit
else: 
    print("Next time enter a valid number, have a good day")
    quit() #if the user decides not to enter a valid integer at all, the program will also quit

random_number = random.randint(0, top_number) #this 2nd variable is created to generate a random number between 0 and the input of the user
guesses = 0 #3rd variable will hold a tally of the score of the total number a guesses a user inputs before guessing the correct number

while True: #creates a loop for our user to guess the random number
    guesses += 1 #the users guess attempts will begin at 1 and everytime the user guesses incorrectly, +1 will be added onto their guess attempts tally
    user_guess = input("Guess the random number: ") #4th variable, will be the users guess number
    if user_guess.isdigit():
        user_guess = int(user_guess) #converts the users sting input into a valid integer
    else:
        print("Please enter a valid number")
        continue #if the user does NOT enter a valid number within the specified range, the loop will restart from here

    if user_guess == random_number:
        break #if the users guess input matches with the randomly generated number, the game will end here
    elif user_guess > random_number:
        print("Sorry, that is too large") #if the users guess number is too large, this message prints and loop restarts
    else:
        print("Sorry, that number is too small") #if the users guess number is too small, this message prints and loop restarts
        

print("Congrats, you have guessed the number = " + str(random_number)) #outputs the correct number that was guessed
print("It took you a total of " + str(guesses) + " guesses") #outputs total amount of attempts the user inputed