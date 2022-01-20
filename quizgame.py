print("Welcome to my computer game") #the game starts with a lovely introduction message

playing = input("Do you want to play? ").lower() #1st variable, the user will specify if they want to play the game or not which will be formatted into lowercase letters

if playing != "yes":
    quit() #if the users input is NOT the word yes, then the program will quit immediately

print("Okay Lets play this game!")
score = 0 #2nd variable will be our score, which will keep tracking of the total amount of questions guessed correctly

answer = input("How many bits does a MAC address contain? ") #our answer variables will store the input from the user
if answer == "48":
    print("Correct!")
    score += 1 #if the users input answer matches the question, +1 will be added to their score
else:
    print("Go back to grade school") #if the user gueses incorrectly, this message will be displayed and they will proceed with the next question

answer = input("How many bits does an IPv6 address contain? ")
if answer == "128":
    print("Correct!")
    score += 1
else:
    print("Go back to grade school")

answer = input("How many bits does in IPv4 address contain? ")
if answer == "32":
    print("Correct!")
    score += 1
else:
    print("Go back to grade school")

print(str(score) + " out of 3 answered correctly") #once all the questions have been answered, the users tally score will be printed out
print("Your overall percentage is " + str((score/3)*100) + "%") # their overall percentage will also be listed