num=int(input("Enter a number"))
i=2
limit=int(num/2)
if num>1:
    while i<=limit:
        #print(i)
        if num%i==0:
            print("its not prime")
            break
        i=i+1
    else:
        print("its prime")
else:
    print("please provide valid number")