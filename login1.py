u_names=['a','b','c','d','e']
passwords=['abc','123','efg','hij','456']
user=input("enter user:")
index=0
for i in u_names:
    if user==i:
        print("user entered")
        pas=input("enter password:")
        if pas==passwords[index]:
            print("welcome",user)
        else:
            print("invalid password")
        break
    index=index+1
else:
    print("user not exist")