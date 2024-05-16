u_names=['a','b','c','d','e']
passwords=['abc','123','efg','hij','456']
user=input("enter user:")
if user in u_names:
    pas=input("enter password:")
    index=u_names.index(user)
    if pas==passwords[index]:
        print("welcome",user)
    else:
        print("invalid password")
else:
    print("invalid user")