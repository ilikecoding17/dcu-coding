from multiprocessing import managers


class Employee():
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        # print(f"{self.first} {self.last}")
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split("-")
        pay = int(pay)
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(f"--> {emp.fullname()}")

dev_1 = Developer("carina", "craciun", 60000, "python")
dev_2 = Developer("diana", "craciun", 60000, "java")

mgr_1 = Manager("roxy", "craciun", 100000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(dev_1.prog_lang)
print(dev_2.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

emp_1 = Employee("isaac", "craciun", 50000)
emp_2 = Employee("adam", "lapinski", 50000)
emp_3 = Employee.from_string('John-Doe-70000')
# print(emp_3.__dict__)
# print(Employee.num_of_emps)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# emp_1.raise_amount = 1.02
# Employee.set_raise_amt(1.05)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)

# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)

import datetime
my_date = datetime.date(2022, 9, 3 )

# print(Employee.is_workday(my_date))
# emp_1_name = emp_1.fullname()
# emp_2_name = Employee.fullname(emp_2)
# print(emp_1_name, emp_2_name)

# print(f"{emp_1.first} {emp_1.last}")

# print(emp_1)
# print(emp_2)

# emp_1.first = "isaac"
# emp_1.last = "craciun"
# emp_1.email = "isaac.craciun@company.com"
# emp_1.pay = 50000

# emp_2.first = "adam"
# emp_2.last = "lapinski"
# emp_2.email = "adam.lapinski@company.com"
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)c