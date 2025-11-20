# A simple and small project of taking  input form the user 
num1 = input("enter the 1st number = ")

symbol = input("Enter what you want to do = ")

num2 = input("Enter the 2nd number = ")

invalid_char = ['#' , '$' , "^" , '&' , ' ()']

if num1  in invalid_char or num2 in invalid_char:
    
    print("invalid input")

else: 
    num1 = int(num1) 
    num2 = int(num2)

if symbol == '+': 

    print(num1 + num2)
    
elif symbol == '-':

    print(num1 - num2)
    
elif symbol == '*':

    print(num1 * num2)
else : 
    
    print("invalid operation")    



