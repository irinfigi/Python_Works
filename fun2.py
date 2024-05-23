#without arguments and without return statement
def demo():
    print("Irin")
demo()
#with arguments and without return statement
def demo1(name):
    print("hi",name)
demo1("bitty")
#without argument and with return statement
def get_pi():
    return 3.14
radius=10
print("area",get_pi()*radius*radius)
#with argument and with return statement
def addTwo(num1,num2):
    total=num1+num2
    return total
print(addTwo(5,10))