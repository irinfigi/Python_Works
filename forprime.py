num=int(input("enter a number:"))
end=int(num/2)
for i in range(2,end):
    if num%i==0:
        print("its not prime")
        break
else:
    print("its prime")