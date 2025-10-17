x=10 #  globel scope
def outer_function():
    x = 5 # enclosing scope
    def inner_function():
        x=2 # local scope
        print(x)
    inner_function()
outer_function()
print(x)

 
 def sum_number(*a)
 total=0
 for number in a:
     total += number 
     return total
 result = sum_number(1,3,4,,5,6,78,43,2)
 print(result)
