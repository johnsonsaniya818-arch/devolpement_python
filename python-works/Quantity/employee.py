import csv

class Employee:

    data:list

    def __init__(self):

        file_path="python-works\\Quantity\\employee_salary_dataset.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

        #print(data)

    def records(self):

        print(len(self.data))

    def males(self):

        exp_5_males=[r.get("Name")for r in self.data if r.get("Experience_Years")>"5" and r.get("Gender")=="Male"]

        print(exp_5_males)

    def finanace(self):

        for r in self.data:

            if r.get("Department")=="Finance":

                print(r)

    def age(self):

        age_name=[r.get("Name")for r in self.data if r.get("Age")>"50"]

        print(age_name)

    def salary(self):

        max_salary={r.get("Name"):r.get("Monthly_Salary")for r in self.data }

        max1=max(max_salary.values())

        maximum=[k for k,v in max_salary.items() if v==max1]

        print(maximum)

    def count(self):

        bangalore_count = 0
        for r in self.data:
            if r.get("City") == "Bangalore":
                bangalore_count += 1
    
        print(bangalore_count)

    def records(self):

        for r in self.data:

            print(self.data[:5])









employee_instance1=Employee()

employee_instance1.records()

employee_instance1.males()

employee_instance1.finanace()

employee_instance1.age()

employee_instance1.salary()

employee_instance1.count()

employee_instance1.count()

employee_instance1.records()
