num1 = int(input("enter the 1st number = "))

symbol = str(input("Enter what you want to do = "))

num2 = int(input("Enter the 2nd number = "))

if symbol == '+': 
    print(num1 + num2)
elif symbol == '-':
    print(num1 - num2)
elif symbol == '*':
    print(num1 * num2)
else : 
    print("Invalid input")    

