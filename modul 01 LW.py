class Employee:
    def __init__(self, name, employee_id, position):
        self.name = name
        self.employee_id = employee_id
        self.position = position

    def calculate_salary(self):
        raise NotImplementedError("This method should be overridden in derived classes")

    def __str__(self):
        return f"{self.name} (ID: {self.employee_id}), Position: {self.position}"

class Worker(Employee):
    def __init__(self, name, employee_id, position, hourly_rate, hours_worked):
        super().__init__(name, employee_id, position)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, employee_id, position, base_salary, bonus):
        super().__init__(name, employee_id, position)
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus

class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_salaries(self):
        for employee in self.employees:
            print(f"{employee}: Salary = {employee.calculate_salary()}")
