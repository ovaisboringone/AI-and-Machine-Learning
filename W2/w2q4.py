class Employee:
    total_employees = 0

    def __init__(self, name):
        self.name = name
        Employee.total_employees += 1

e1 = Employee("Ali")
e2 = Employee("Ahmed")
e3 = Employee("Omar")

print(Employee.total_employees)