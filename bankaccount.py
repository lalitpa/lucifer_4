class BankAccount:
    def __init__(self,accountno,accounttype,accountopeningdate,accountholdersname,panno,accountholdersaddress,accountbalance):
        self.accountno=accountno
        self.accounttype=accounttype
        self.accountopeningdate=accountopeningdate    
        self.accountholdersname=accountholdersname
        self.panno=panno
        self.accountholdersaddress=accountholdersaddress
        self.accountbalance=accountbalance
    def debit(self,amount):
        self.amount=amount
        if self.amount>self.accountbalance:
            print('error')
        else:
            self.accountbalance=self.accountbalance-self.amount
    def credit(self,amount):
        self.amount=amount
        self.accountbalance=self.accountbalance+self.amount    
    def withdrawcash(self,amount):
        self.amount=amount
        if self.amount>self.accountbalance:
            print('error')
        else:
            self.accountbalance=self.accountbalance-self.amount
    def depositcash(self,amount):
        self.amount=amount
        self.accountbalance=self.accountbalance+self.amount
    def display(self):
         print('ACCOUNT NO.',self.accountno)
         print('ACCOUNT TYPE',self.accounttype)
         print('DATE OF OPENING',self.accountopeningdate)
         print("ACCOUNT HOLDER'S NAME",self.accountholdersname)
         print('PAN NO.',self.panno)
         print('ADDRESS',self.accountholdersaddress)
         print('ACCOUNT BALANCE',self.accountbalance)
s=BankAccount(3658951456320,'Savings','03/05/2019','LALIT',456321,'hansnagar',5000)
s.credit(100000000)
s.withdrawcash(1000000000000)
s.display()
