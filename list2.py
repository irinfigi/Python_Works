max_limit=5
age_list=[]
i=1
while i<=max_limit:
    age=int(input("Enter your age:"))
    age_list.append(age)
    i=i+1
print(age_list)
j=0
age_sum=0
while j<len(age_list):
    age_sum=age_sum+age_list[j]
    print(age_list[j])
    j=j+1
avg=age_sum/len(age_list)
print("the avg age of employee",avg)
