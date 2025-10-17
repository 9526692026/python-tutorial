try:
    with open('output.txt', 'w') as file:
        file.write("Hello World")
    print("File written successfully!")
except PermissionError:
    print("Permission denied!")
