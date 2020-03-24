n = input("enter the name  :")

l = (n.lower().count('o'))
s = (n.lower().count('x'))
if (l == s):
    print("true")
elif (l != s):
    print("false")
else: print("true")


