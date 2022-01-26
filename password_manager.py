from asyncore import write
from distutils.file_util import write_file
from cryptography.fernet import Fernet #This module is required to be imported in order to encrypt / generate keys

#Below, we will define a new function for generating our key file, which will only be used once initially
# def create_key(): #creating a new function which will generate our encryption key
#     key = Fernet.generate_key() #this key variable will be used to generate our key from the fernet module
#     with open ("key.key",  "wb") as key_file: #we will open a new text file and write to it in bytes
#         key_file.write(key) #when we write to the keyfile variable, we will input the key that was generated from fernet module

#create_key() # CALL / RUN THIS FUNCTION ONCE! once you have generated your new key.key file you do NOT need to run this function again

def load_key(): #creating a new function which will load the encryption key we just generated in the last function
    file = open("key.key", "rb") #this variable will be used to open the key.key file in read bytes mode only
    key = file.read() #sets the readable version of the file to a variable named key
    file.close() #remember to manually close the file if not specified with this method
    return key #returns the values within the key variable we created, which will be the key.key read file contents

key = load_key() #stores the load_key function into a variable named key
fer = Fernet(key) #stores and formats the key variable as a Fernet class into a variable named fer

def add():
    usrname = input("Enter New Username: ") #will take user input to store a username variable
    password = input("Enter New Password: ") #will take user input to store a password variable

    with open("passwords.txt", "a") as f: #if not already created, will create AND append to the passwords.txt file and stores it as a variable named f
        f.write(usrname + " | " + fer.encrypt(password.encode()).decode() + "\n") #will write a new line into the passwords.txt with a username column, password column, and a carriage return at the end for readability

def view():
    with open("passwords.txt", "r") as f: #opens the passwords.txt file as read only and stores it as a variable named f
        for line in f.readlines(): #loop and read through every line in the f variable
            data = line.rstrip() #this variable will read each line in the passwords.txt file and remove the carriage returns at the end
            user, passw = data.split("|") #creates two variables from the data variable, and splits the data in two whenever a | is discovered
            print("Username: " + user + "| Password:" + fer.decrypt(passw.encode()).decode()) #prints out the results in terminal of our username and password data into a readable format
            

while True:
    mode = input("Would you like to add new / view existing passwords? (add / view) or enter Q to quit: ").lower() #takes input from the user and executes one fo the specificed functions below. Ensures all user input is lowercase
    if mode == "q": #entering Q or q will break the loop and quit the program
        break

    if mode == "add": 
        add() #will initialize the add() function
    elif mode == "view":
        view() #will initialize the view() funtion
    else:
        print("Not a valid option")

