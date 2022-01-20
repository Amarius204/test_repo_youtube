print("Welcome to my computer game")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()

print("Okay Lets play this game!")
score = 0

answer = input("How many bits does a MAC address contain? ")
if answer == "48":
    print("Correct!")
    score += 1
else:
    print("Go back to grade school")

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

print(str(score) + " out of 3 answered correctly")
print("Your overall percentage is " + str((score/3)*100) + "%")