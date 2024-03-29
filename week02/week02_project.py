"""
Store Employee Database and Payroll Program
(C) Giles Cooper 2024
MIT License
"""
import pickle

import payroll

DEFAULT_DB_NAME = 'payroll.db'

menu = {
    "M":"Add New Manager",
    "A":"Add New Associate",
    "R":"Give a manager a raise",
    "r":"Give an associate a raise",
    "Y":"Increment a manager's years employed",
    "y":"Increment an associate's years employed",
    "L":"Show list of all workers",
    "I":"Print info on a worker",
    "S":"Print a manager's Salary",
    "P":"Print an associate's Pay",
    "Q":"Save and Quit"
}

#dictionary to ease access to StoreWorker employee_number
#{employee_number:store_worker_object}
managers={}
associates={}

# we end up listing workers a lot, the following functions help with that.
# sometimes we want just the managers, sometimes just associates
def print_managers():
    for id, worker in managers.items(): print(f"{id} : {worker.name}")

def print_associates():
    for id, worker in associates.items(): print(f"{id} : {worker.name}")

def print_workers():
    # sometimes both. Smooth them together and re-sort them.
    workers = dict(sorted({**associates, **managers}.items()))
    if not workers: print("No workers have been entered.")
    else:
        for id, worker in workers.items(): print(f"{id} : {worker.name}")

# create a new worker of type "A" or "M"
def create_new_worker(worker_type):
    print("What is the new worker's name?")
    newname = input()
    # get their starting pay. blank or invalid data gives minimum wage.
    if worker_type == "A":
        print("What is the hourly payrate?")
        pay=input()
        try: pay = float(pay)
        except: new = payroll.Associate(newname)
        else: new = payroll.Associate(newname, pay)
        associates[new.get_employee_number()]=new
    elif worker_type == "M":
        print("What is the weekly pay?")
        pay=input()
        try: pay = float(pay)
        except: new = payroll.Manager(newname)
        else: new = payroll.Manager(newname, pay)
        managers[new.get_employee_number()]=new
    print(f"{type(new)} created.\n{new}")


# give a raise to either manager or associate
def give_raise(worker_type): 
    print("which worker would you like to give a raise?  (by number)")
    if worker_type == "R":
        period = "week"
        print_managers()
    elif worker_type == 'r':
        period = "hour"
        print_associates()
    worker=input("  >>  ")

    # validate worker number and worker type
    try: 
        worker=int(worker)
        if worker_type == "R" and worker not in managers.keys(): 
            raise KeyError
        if worker_type == "r" and worker not in associates.keys(): 
            raise KeyError
    except: 
        # could do seperate excepts for error type but this is a good catch-all.
        print("invalid worker")
    else:
        # merge associates and manager dictionaries:
        workers = {**associates, **managers}
        # okay everything is validated now, and the rest of the function is
        # agnostic to the manager/associate distinction:
        print(f"How much should the {period}ly pay raise be?")
        # PEP8 says append a trailing underscore when variable name 
        # collides with a reserved keyword:
        raise_ = input()
        try: 
            raise_ = float(raise_)
            if raise_ < 0: raise ValueError
        except: 
            print("invalid value for raise")
        else: 
            # apply the raise to the worker:
            workers[worker].give_raise(raise_)
            print(f"Done. {workers[worker]}")

# increment years, based on worker type.
# since both manager and associate have the same method to
# increase their tenure, this distinction is unnecessary,
# but it was written as two seperate bullet points in 
# Part 2 of the week 2 project details
def increment_years(worker_type):
    if worker_type == "Y":
        print_managers()
    elif worker_type == "y":
        print_associates
    print("Which workers to give a raise? (by number)")
    worker = input()
    try: 
        worker=int(worker)
        if worker_type == "Y" and worker not in managers.keys(): 
            raise KeyError
        if worker_type == "y" and worker not in associates.keys(): 
            raise KeyError
    except: print("Invalid worker.")
    else: 
        workers = {**associates, **managers}
        workers[worker].increase_years()

#print worker info
def print_info():
    print_workers()
    print("Which worker would you like information on? (by number)")
    try:
        worker_number = int(input())
        workers = {**associates, **managers}
        if worker_number not in workers:
            raise IndexError
    except:
        print("not a valid worker number")
    else:
        print(workers[worker_number])
    
# each function I am more and more annoyed at my own coding pattern
# but at this point I'm invested so might as well just finish it
def print_pay(worker_type):
    if worker_type == "S":
        period="week"
        print_managers()
    elif worker_type == "P":
        period="hour"
        print_associates()
    print("Which worker would you like to see payroll info? (by number)")
    worker = input()
    try: 
        worker=int(worker)
        if worker_type == "S" and worker not in managers.keys(): 
            raise KeyError
        if worker_type == "P" and worker not in associates.keys(): 
            raise KeyError
    except: print("Invalid worker.")
    else: 
        workers = {**associates, **managers}
        if worker_type == "S":
            pay = workers[worker].get_salary()
        elif worker_type == "P":
            pay = workers[worker].get_hourly_rate()
        # finally a decent line of code:
        print(f"{workers[worker].name}: ${pay}/{period}")
            
# save payroll database to file
def save_data():
    workers = {**associates, **managers}
    try:
        with open('payroll.db', 'wb') as payroll_db:
            pickle.dump(workers, payroll_db)
    except:
        print("database could not be saved for whatever reason.")
    
# load payroll database from file:
def load_data():
    print("Please enter database file name to load...")
    if input() != DEFAULT_DB_NAME: print("incorrect.")
    try:
        with open(DEFAULT_DB_NAME, 'rb') as payroll_db:
            db = pickle.load(payroll_db)
            for id in db:
                if isinstance(db[id], payroll.Associate):
                    associates[id]=db[id]
                elif isinstance(db[id], payroll.Manager):
                    managers[id]=db[id]
        print("Previous payroll data loaded...")
    except:
        pass # say nothing if no data found

def main():
    load_data()
    while True:
        # display options menu:
        for key,val in menu.items(): print(f"{key} ). {val} ")
        option = input("Select from menu:  >>  ")

        if option not in menu.keys():
            print("command not recognized...")
            if option.lower() in menu.keys() or option.upper() in menu.keys():
                print("input is case-sensitive!")
            continue

        elif option == "M" or option == "A":
            create_new_worker(option)
        elif option == "R" or option == "r":
            give_raise(option)
        elif option == "Y" or option == "y":
            increment_years(option)
        elif option == "L":
            print_workers()
            input("(press Enter to continue)")
        elif option == "I":
            print_info()
        elif option == "S" or option == "P":
            print_pay(option)
        elif option == "Q":
            print("Okay bye")
            save_data()
            break
if __name__=="__main__": main()