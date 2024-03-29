"""
Store Employee Database and Payroll Program
(C) Giles Cooper 2024
MIT License
"""
import payroll
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
}

#dictionary to ease access to StoreWorker employee_number
#{employee_number:store_worker_object}
managers={}
associates={}

def print_managers():
    for id, worker in managers.items(): print(f"{id} : {worker.name}")

def print_associates():
    for id, worker in associates.items(): print(f"{id} : {worker.name}")

def print_workers():
    workers = {**associates, **managers}
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
        for id, worker in associates.items(): 
            print(f"{id} : {worker.name}")
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

def main():
    while True:
        for key,val in menu.items():
            print(f"{key} ). {val} ")
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
        elif option == "I":
            pass # TODO: Print info on a worker
        elif option == "S":
            pass # TODO: Print a manager's Salary
        elif option == "P":
            pass # TODO: Print an associate's Pay

if __name__=="__main__": main()