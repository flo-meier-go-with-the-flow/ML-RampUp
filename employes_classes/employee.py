from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def print_salary(self, salary):
        print(f'Name: {self.name}, Salary: {salary}')
