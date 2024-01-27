class Employee:
    number_of_employees = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.number_of_employees += 1

    def average_salary(self, *salaries):
        return sum(salaries) / len(salaries)


class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department, hours_worked):
        super().__init__(name, family, salary, department)
        self.hours_worked = hours_worked


#instances
instance1 = Employee("Ram", "Family1", 70000, "Front endeveloper")
instance2 = Employee("Raju", "Family2", 60000, "back end developer")


full_time_employee = FullTimeEmployee("Ramesh", "Family3", 70000, "Java Developer", 60)

# Call member functions

print(f"Number of Employees: {Employee.number_of_employees}")
average_salary_employee = instance1.average_salary(instance2.salary)
print(f"Average Salary of Employees: {average_salary_employee}")

average_salary_full_time_employee = full_time_employee.average_salary(instance1.salary, instance2.salary)
print(f"Average Salary of Employees including FullTimeEmployee: {average_salary_full_time_employee}")