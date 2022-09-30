from employes_classes.fulltimeemployee import FullTimeEmployee
from employes_classes.hourlyemployee import HourlyEmployee

ef1 = FullTimeEmployee('John', 8000)
ef1.print_salary(ef1.get_salary())
eh1 = HourlyEmployee('Peter', 40)
eh1.print_salary(eh1.get_salary(160))