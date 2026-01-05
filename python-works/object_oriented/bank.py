class Bank:

    acc_no : str

    acc_name : str

    branch : str

    balance : int


    def __init__(self,acc_no,acc_name,branch,balance):

        self.acc_no = acc_no

        self.acc_name = acc_name

        self.branch = branch

        self.balance = balance

    def display(self):

        print(self.acc_no,self.acc_name,self.branch,self.balance)

    def deposit(self,amount):

        self.balance += amount

        print("total amount after adding the deposit into balance amount",self.balance)

    def withdrawal(self,withd):

        if(self.balance>withd):

            self.balance-= withd

            print(f"total amount of{self.acc_name} after deducting the withdrawal amount from balance{self.balance}")

        else:

            print("transaction failed")

bank_c1=Bank("de2","anitha","kochi",500000)

bank_c2=Bank("ac14","anu","thrissur",200000)

bank_c2.display()

bank_c2.deposit(50000)

bank_c1.display()

bank_c2.withdrawal(300)