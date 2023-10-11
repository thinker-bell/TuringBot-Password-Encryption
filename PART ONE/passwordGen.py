#Python program to generate a strong password of a given length.
#=============================================================
#Import required libraries - random and os (operating system).
import random
import os

#Compose a function to generate a password of a defined 'length'.

def generate_password(input_password):

#Define characters to be used in the construction of the password.
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+"
    password = ""

    random.seed(input_password)
   
    #Apply a for loop to implement the iteration: password = password + random choice
    #of defined characters using function random.
    for i in (input_password):
        password += random.choice(characters)
    return password #Return the result

input_password = str(input("Please enter your user password: "))
#Define the length of the password specified by the user.
#length = int(input("Enter a password length: "))
#length = len(input_password)

#Generate password using password generating function
password = generate_password(input_password)
#and print the password on the screen.
print("Your new password is:", password)

#Write the result to file in 'Documents'.
#Set the path.
#documents_path = os.path.expanduser("~\Documents")

#Write the password in file 'password.txt'.
#file_path = os.path.join(documents_path, "password.txt")
file_path = ("password.txt")

#Open file and write result.
with open(file_path, "w") as file:
    file.write(password)

#State where file has been saved.
print("Password saved to:", file_path)

input('Press ENTER to exit')