mylist = []
limit = int(input("Enter number of elements:"))
for i in range(1 ,limit+1):
    n = int(input("Enter the elements:"))
    mylist.append(n)
mylist.sort()
print("second largest", mylist[-2])