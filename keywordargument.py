# def key(**abc):
#     print(abc)
# key(a=1,b=2,c=3)

# def a(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# a(name="alice",age="30",place="palakkad")

# def b(**abc):
#     return f"name is {abc['name']} and my age is {abc['age']} and my place is {abc['place']}"
# print(b(name="jhon",age="20",place="palakkad"))

# def a(*args,**kwargs):
#     print("string",args)
#     print("num",kwargs)
# a(1,2,3,name="jhone",age="30",place="palakkad")
    
#     def a(abc,*args,**kwargs):
#     print("vegattt",abc)
#     print("string",args)
#     print("num",kwargs)
# a(1,2,3,name="jhone",age="30",place="palakkad")

def price(**item):
    for key in item.key():
        print("item name is {item[key]} this price is {key}")
price(phone=2000,tv=400000)