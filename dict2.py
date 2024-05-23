login_dict={'Irin':'abc','Juval':'345a','Tina':'asd'}
username=input("Enter name:")
if username in login_dict.keys():
    password=input("enter pass:")
    if password==login_dict[username]:
        print("welcome",username)
    else:
        print("incorrect pass")
else:
    print("invalid user")