# (c) Giles Cooper 2024

class ChangePurse:
    
    def __init__(self, amount=0):
        self.__amount = amount

    def __str__(self):
        return f"${self.__amount:.2f}"

    def addChange(self, amount):
        self.__amount += amount

    @property
    def balance(self):
        return self.__amount

    def removeChange(self, amount):
        self.__amount -= amount
        return amount # so it works like pop()

    def __lt__(self, purse):
        if self.__amount < purse.balance: return True
        else: return False

    def __gt__(self, purse):
        if self.__amount > purse.balance: return True
        else: return False

    def __eq__(self, purse):
        if self.__amount == purse.balance: return True
        else: return False