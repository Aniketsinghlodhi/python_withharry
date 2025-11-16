# Static & Class Methods
# In Python, methods within a class can be of three main types:

# Instance Methods: These are the most common type of method. They operate on instances of the class (objects) and have access to the instance's data through the self parameter.
# Class Methods: These methods are bound to the class itself, not to any particular instance. They have access to class-level attributes and can be used to modify the class state. They receive the class itself (conventionally named cls) as the first argument.
# Static Methods: These methods are associated with the class, but they don't have access to either the instance (self) or the class (cls). They are essentially regular functions that are logically grouped within a class for organizational purposes.

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method    
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Methods 
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34355)
# print(Employee.company)
# print(Employee.name) # this will throw an error
# e1.print_info()
# e2.print_info()

# print(e2.sum(5, 23))
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)