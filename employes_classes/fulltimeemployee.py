from employes_classes.employee import Employee


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_salary(self):
        return self.salary








