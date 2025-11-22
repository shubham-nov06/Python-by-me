# A simple  password generator project 
import random 
import string 

length = int(input("Enter password length = "))

char = string.ascii_letters + string.digits 
password = "".join(random.choice(char) for i in range (length))

print("Generated password = " , password)
