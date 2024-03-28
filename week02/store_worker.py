"""
Store Employee Database and Payroll Program
(C) Giles Cooper 2024
MIT License
"""
# federal minimum pay
MINIMUM_WAGE = 7.25 
MINIMUM_SALARY = 684

class StoreWorker:
    emp_number = 0
    # potentially confusing naming convention, maybe "employee_index" ?

    def __init__(self, newname): 
        StoreWorker.emp_number += 1
        self.name = newname
      
        self.__employee_number = StoreWorker.emp_number
        self.__years = 0
        self.__bonus_so_far = []

    def get_employee_number(self):
        return self.__employee_number
    
    def get_years(self):
        return self.__years
    
    def increase_years(self):
        self.__years += 1

    def give_bonus(self, amount):
        self.__bonus_so_far.append(amount)

    def get_bonus(self):
        return self.__bonus_so_far
    
    def __str__(self):
        return f"<{self.name}: Emp#{self.get_employee_number()}, {self.get_years()} yrs.>"


# an hourly worker
class Associate(StoreWorker):
    # if they forgot to ask about pay, start at minimum wage
    def __init__(self, newname, hourly_rate=MINIMUM_WAGE):
        super().__init__(newname)
        self.__hourly_rate = hourly_rate

    # give a raise to the hourly rate
    def give_raise(self, amount):
        if amount < 0:
            print(f"{self.name} does not accept the pay cut.")
            raise ValueError("The associates rally and form a union!")
        self.__hourly_rate += amount

    def increase_years(self):
        super().increase_years()
        self.give_bonus(50)
        # maybe 4 hours' pay would be better.. $50 doesn't scale well

    def get_hourly_rate(self):
        return self.__hourly_rate
    
    # If you forget to clock out, you will lose your overtime
    def calc_weekly_pay(self):
        return self.__hourly_rate * 40
    
    def __str__(self):
        return super().__str__() + f":<${self.__hourly_rate:.2f}/hr>"
    

class Manager(StoreWorker):
    # if they forget to negotiate pay in the interview, start at minimum salary
    def __init__(self, newname, newsalary=MINIMUM_SALARY):
        super().__init__(newname)
        self.__weekly_salary = newsalary
           
    def give_raise(self, amount):
        self.__weekly_salary += amount

    def increase_years(self):
        super().increase_years()
        if self.get_years() % 5 == 0: self.give_bonus(200)

    def get_salary(self):
        return self.__weekly_salary
    
    def __str__(self):
        return f"{super().__str__()} <${self.__weekly_salary}/wk>"
