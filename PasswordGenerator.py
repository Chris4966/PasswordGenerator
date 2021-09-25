import random
import os
import time

# Function to generate random char
def GenerateChar():
    # Selects a random type of char; either upper case letters, lower case letters, or numbers
    UCLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LCLetters = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "0123456789"

    CharType = random.randint(1, 3)

    # Selects a random char from the appropriate string and returns it
    if CharType == 1:
        index = random.randint(0, len(UCLetters)-1)
        return UCLetters[index]
    elif CharType == 2:
        index = random.randint(0, len(LCLetters)-1)
        return LCLetters[index]
    else:
        index = random.randint(0, len(Numbers)-1)
        return Numbers[index]

# Function to write the password to a text file
def WriteToFile(filename, password):
    PWFile = open(filename, "a")
    PWFile.write("Generated Password: " + password + "\n")
    PWFile.close()

    # Prints the file path to console
    path = os.path.abspath(filename)
    dir = os.path.dirname(path)
    print("Password saved in file: " + dir + "/" + filename)

# Password list and length
print ("---Password Generator by Chris RH--- \nPlease select a desired length between 8 and 20: ")
PasswordLength = int(input())

if PasswordLength >= 8 and PasswordLength <= 20:

    Password = []

    # Calls the GenerateChar(function) for each iteration and appends it to the list
    for i in range(PasswordLength): 
        Password.append(GenerateChar())

    # Prints the generated password to console and saves it to a file
    print("".join(Password))
    WriteToFile("passwords.txt", "".join(Password))
    input()

else:
    print("Error: invalid input!")
    input()