# A simple project of tempearature covertor 
print(" 1 - Celsius to Fahrenheit ")
print(" 2 - Fahrenheit to Celsius ")

ch = int(input("Choose the option"))

if ch== 1 :
    c = float(input("Celcius"))
    print("Fahrenheit = " , (c *9/5) + 32)
    
elif ch==2:
    f = input("Fahrenheit")
    print("Fahrenheit = " , (f - 32) * 5/7)