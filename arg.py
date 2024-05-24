    # #positional arguments
# def demo(a,b,c):
#     print(a,b,c)
#     print(a+b+c)
# demo(1,2,3)
    # #keyword arguments
# def demo1(name,age,salary):
#     print("hi",name)
#     print(salary)
#     print(age)
# demo1(salary=25000,name='irin',age=22)
    #default argument
# def numbers(a,b,c=10,d=20):
#     print(a,b,c,d)
#     print(a+b+c+d)
# numbers(1,2,3)
    #arbitary positional argument
# def numbers(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     print(sum)
# numbers(1,2,3,4)
    #arbitarary keyword argument
def student_details(**details):
        print(details)
        for key,value in details.items():
            print(key,":",value)
student_details(name='irin',age=23,slary=25000,loc="thrissur")

