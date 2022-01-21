import random
from urllib.parse import uses_relative

user_wins = 0 #1st variable will keep track of the users score
computer_wins = 0 #2nd variable will keep track of the computers score
options = ["rock","paper","scissors"] #3rd variable will create a list, which will store our 3 string options for rock, paper and scissors

while True:
    user_input = input("Choose Rock / Paper / Scissors to initiate your turn, or enter Q to quit: ").lower()
    if user_input == "q":
        break #if the user types in the letter Q, the loop will break and the game will quit
    if user_input not in options: #used our options variable containing our 3 strings as opposed to 3 seperate if statements for cleanliness
        continue #if the user types in anything OTHER than rock, paper, or scissors then the loop will restart

    random_number = random.randint(0,2) # new variable for random number generator. rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number] #this variable will assign the approriate index number to one of the 3 strings
    print("Computer picked " + str.capitalize(computer_pick) + ".") #prints out the computers rnadomly generated pick

    if user_input == "rock" and computer_pick == "scissors": #if statement will compare 2 conditions that must be true
        print("Congrats! you won!")
        user_wins += 1 #add +1 to the users score
    elif user_input == "scissors" and computer_pick == "paper":
        print("Congrats! you won!")
        user_wins += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("Congrats! you won!")
        user_wins += 1
    elif user_input == computer_pick: #if the user and computer pick that same string, a stalemate occurs
        print("Stalemate, lets try again!")
    else:
        computer_wins += 1 #if none of the above conditions are meet, the computer wins by default
        print(str.capitalize(computer_pick)+ " beats " + str.capitalize(user_input) + " . You lost!")

    print("Your score: " + str(user_wins) + " ,Computer score: " + str(computer_wins)) #at the end of the loop or game round, the user vs. the computer score is printed
        

print("Goodbye!") #when the user enters Q and decides the quit the game, this goodbye message prints out
