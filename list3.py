max_list=[2,23,45,67,80,100]
max=0
j=0
while j<len(max_list):
    if max_list[j]>max:
        max=max_list[j]
    j=j+1
print("the biggest is",max)
