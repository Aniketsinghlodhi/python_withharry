class Employee:
    company = "Apple" #This is class attribute


    def __init__(self, salary,name,bond, company ):
         self.salary = salary # create an instance attribute of salary and assign with salary 
         self.name = name 
         self.bond = bond 
         self.company = company

    def  get_salary(self):
         return self.get_salary
    def get_info (self):
         print(f"Name of the employeeis {self.name}.salary is {self.salary}. the bond is for {self.bond }years ")

e1 = Employee(10000, "Ruda" , 44, "tesla")
print(e1.company) # will always print instance attribute whenever present 


# Object introspection 
print(dir(e1))
print(Employee.company())# This will always print the class attribute