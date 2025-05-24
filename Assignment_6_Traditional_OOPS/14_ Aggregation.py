# Employee class - independent
class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title  # Employee's job title

    def get_details(self):
        return f"Employee Name: {self.name} | Job Title: {self.job_title}"

# Department class - has an Employee, but doesn't own it
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: uses existing employee object

    def show_department_info(self):
        return f"Department: {self.dept_name} | {self.employee.get_details()}"

# Create an Employee object independently
emp = Employee("Saima Amjad", "Web Developer")

# Pass the Employee to Department (aggregation)
dept = Department("IT", emp)

# Display department info
print(dept.show_department_info())