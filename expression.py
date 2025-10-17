import re

# re.match

# text="hallo world"
# match=re.match(r"hallo",text)
# print(match)

# re serch

# text = "hallo world"
# match = re.search(r"hallo",text)
# print(match)

# re.findall

# text="the price is 45 dollers.30 cent,and 50 rupess"
# numbers=re.findall(r"\d",text)
# print(numbers)

# re.sub

# text="hello123,welcome456!"
# new=re.sub(r"\d+","number",text)
# print(new)


# re.split

# text = "apple, orange, banana, grape" 
# fruits = re.split(r"[;,]", text) 
# print(fruits)  

# re.compile

# text = "123 apples and 456 oranges" 
# pattern = re.compile(r"\d+") 
# match = pattern.findall(text) 
# print(match)  

# text="jhon:34,alice:45,bob:24"
# match=re.findall(r"(\w):(\d+)",text)
# print(match)

# text = "HELLO world"
# match = re.search(r"hello",text,re.IGNORECASE)
# print(match)
 
text = """first line
second line
third line"""
 
print(re.findall(r"^t\w+", text, re.MULTILINE))

 
