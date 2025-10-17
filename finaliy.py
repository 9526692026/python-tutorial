try:
    num = int(input("Enter a number: ")) 
    result = 10 / num 
except ZeroDivisionError: 
    print("Division by zero is not allowed!") 
else: 
    print(f"The result is {result}") 
finally: 
    print("This will always be printed.") 
