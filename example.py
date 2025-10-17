list2=[1,2,3,45,6,5,7,8,9,2,3,4,10]
a=max(list2)
b=min(list2)
print(a)
print(b)

# 2
c=list2[::-1]
print(c)

# 3

d=list2.count(3)
print(d)

# 4

set1=(set(list2))
list1=(list(set1))
print(list1)

# 5

a=[2,3,4,5,6]
b=["a","s","c"]
c=a+b
print(c)

# 7

a="malayalam"
if a==a[::-1]:
    print("palindrom")
elif a !=a[::1]:
    print("not palindrom")

# 9
a=["apple","banana","orange","cherry"]
b=(tuple(a))
a=(list())
print(list1)