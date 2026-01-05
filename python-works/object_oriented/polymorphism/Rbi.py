class Rbi:

    def gold_loan_rate(self):

        print("Gold Loan Rate",8.5)

    def home_loan_rate(self):

        print("Hoome loan Rate",9.2)

    def car_loan_rate(self):

        print("Car Loan Rate",8.5)

class Hdfc(Rbi):

    def gold_loan_rate(self):

        print("Gold Loan Rate",9.5)

    def home_loan_rate(self):

        print("Hoome loan Rate",10)

    def car_loan_rate(self):

        print("Car Loan Rate",9.7)

hdfc_instance1=Hdfc()

hdfc_instance1.gold_loan_rate()

hdfc_instance1.home_loan_rate()

hdfc_instance1.car_loan_rate()