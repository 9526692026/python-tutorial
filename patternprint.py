# rows = 5
# for a in range(1,6):
#     print("*" *a)
    
# rows = 6
# for a in range(6,1,-1):
#     print("*" *a)
    
    
# rows = 5
# for a in range(rows +1):
#     print(" "*(5-a),"*"*(2*a+1))
    
    
    
# rows = 8
# for a in range(rows +1):
#     print(" "*(rows-a),"*"*(2*a+1))    
# for i in range(rows, -1,-1):
#     print(" "*(rows-i),"*"*(2*i+1))



a="the cat and the  dog"
print("the",a.count("the"),"cat",a.count("cat"),"and",a.count("and"),"dog",a.count("dog"))


rows=5
for a in range(1,rows+1):
    for j in range(1,a+1):
        print(j,end=" ")
    print()    