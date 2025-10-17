# file = open("sample.txt","r")
# # content = file.read()
# # print(content)

# for x in file:
#     print(x.strip())
# file.close()

# file=open("sample.txt","r")
# l=file.readline().strip()
# a=file.readline()
# print(l)
# print(a)
# file.close()

# file=open("sample.txt","w")
# line=["hello\n","welcome to jumanji\n"]
# file.writeline(line)
# print(line)
# file.close()


# append( add elemet)


# file=open("sample.txt","a")
# file.write("sreee.\n")
# file.close()


# seek(first elemet remove)


file=open("sample.txt","r")
file.seek(5)
print(file.read())
file.close()
