class Employee:
    def __init__(self, name, salary, ssn):  # constructor
        self.name = name        # public
        self._salary = salary   # protected
        self.__ssn = ssn        # private

emp = Employee("saima", 50000, "1234567")

print(emp.name)            
print(emp._salary)         
print(emp._Employee__ssn)  





