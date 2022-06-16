class Accounts:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())
    
    def withdraw(self,amount):
        self.balance=self.balance-amount

    def deposite(self,amount):
        self.balance=self.balance+amount
    

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Accounts):
    """This class generates checking accounts objects"""
    type="Checking"
    def __init__(self,filepath,fee):
        Accounts.__init__(self,filepath)
        self.fee=fee

    def transfer(self,amount):
        self.balance=self.balance-amount-self.fee


jacks_check=Checking("jack.txt",8)
jacks_check.transfer(2200)
print(jacks_check.balance)
jacks_check.commit()
print(jacks_check.type)

jhon_check=Checking("jhon.txt",8)
jhon_check.transfer(228)
print(jhon_check.balance)
jhon_check.commit()
print(jhon_check.type)