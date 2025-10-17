def highorder(a,b,subs):
    return subs(a,b)

def plus(a,b):
    return a+b

def multiply(a,b):
    return a*b

def substraction(a,b):
    return a-b

def division(a,b):
    return a/b

print(highorder(7,2,plus))
print(highorder(3,9,multiply))
print(highorder(50,10,division))
print(highorder(15,6,substraction))