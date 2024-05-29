class Employee:
    company='ABCD'
    location='Thrissur'
    def __init__(self,id,name,salary):
        self.empid=id
        self.empname=name
        self.empsalary=salary
    def getdetails(self):
        print(self.empid,self.empname,self.empsalary)
obj1=Employee('emp1','irin',30000)
obj2=Employee('emp2','andrea',20000)
obj3=Employee('emp3','tina',40000)
obj1.getdetails()
obj2.getdetails()
obj3.getdetails()
    