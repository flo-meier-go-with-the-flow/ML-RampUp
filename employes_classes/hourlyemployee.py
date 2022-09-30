from employes_classes.employee import Employee


class HourlyEmployee(Employee):
    def __init__(self,name, hourly_rate):
        super().__init__(name)
        self.hourly_rate=hourly_rate

    def get_salary(self,working_hours):
        return self.hourly_rate*working_hours



