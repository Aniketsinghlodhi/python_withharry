class Employee:
    def __init__(self, salary,name,bond ):
         self.salary = salary # create an instance attribute of salary and assign with salary 
         self.name = name 
         self.bond = bond 

    def  get_salary(self):
         return self.get_salary
    def get_info (self):
         print(f"Name of the employeeis {self.name}.salary is {self.salary}. the bond is for {self.bond }years ")

e1 = Employee(10000, "Ruda" , 44)
e1.get_info()