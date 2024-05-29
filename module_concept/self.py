class Employee:
    company='ABCD'
    loc='Thrissur'
    def __init__(self,id,name,salary):
        self.emp_id=id
        self.emp_name=name
        self.emp_salary=salary
    def get_details(self):
        print(self.emp_id,self.emp_name,self.emp_salary)
obj1=Employee('emp1','irin',23000)
obj2=Employee('emp2','andrea',22000)
obj3=Employee('emp3','tina',25000)
obj1.get_details()
obj2.get_details()
obj3.get_details()