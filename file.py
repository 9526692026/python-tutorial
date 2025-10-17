file=input("enter youer file name:")
try:
    with open(file,'r') as files:
        content=files.read()
    print(content)
except FileNotFoundError:
    print("Error")