import random
import os

def GenerateChar():
    CharType = random.randint(1, 3)

    UCLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LCLetters = "abcdefghijklmnopqrstuvwxyz"
    Numbers = "0123456789"

    if CharType == 1:
        index = random.randint(0, len(UCLetters)-1)
        return UCLetters[index]
    elif CharType == 2:
        index = random.randint(0, len(LCLetters)-1)
        return LCLetters[index]
    else:
        index = random.randint(0, len(Numbers)-1)
        return Numbers[index]

def WriteToFile(filename, password):
    PWFile = open(filename, "a")
    PWFile.write("Generated Password: " + password + "\n")
    PWFile.close()

    path = os.path.abspath(filename)
    dir = os.path.dirname(path)
    print("Password saved in file: " + dir + "/" + filename)

PasswordLength = 10
Password = []

for i in range(PasswordLength):
    Password.append(GenerateChar())

print("".join(Password))
WriteToFile("passwords.txt", "".join(Password))