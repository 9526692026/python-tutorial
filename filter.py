# numbers=[1,2,3,4,5,6,7,8,9,10]
# a=filter(lambda x:x%2==0,numbers)
# print(list(a))

# from functools import reduce
# number=[1,2,3,4,5,6,7,8,9,10]
# a=reduce(lambda x,y:x+y,number)
# print(a)

# from functools import reduce
# number=[]
# a=reduce(lambda x,y:x+y,number ,0)
# print(a)

# a="hello world this is js"
# b=a.replace(" ","-")
# print(b)

rows = 5
for a in range(1,6):
    print("*" *a)
    
rows = 6
for a in range(6,1,-1):
    print("*" *a)