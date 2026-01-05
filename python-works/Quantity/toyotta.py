import csv

class Toyotta:

    data:list

    def __init__(self):

        file_path="python-works\\Quantity\\toyota.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

    def length(self):

        print(len(self.data))

    def price(self):

        d1=[r.get("price")for r in self.data if r.get("year")=="2016"]

        print(d1)

    def transmission(self):

        d3=[r.get("model")for r in self.data if r.get("transmission")=="Manual"]

        print(d3)

    def milege(self):

        d4=[r.get("price")for r in self.data if r.get("mileage")>"20000"]

        print(d4)

    def model(self):

        d3={r.get("model"):r.get("price")for r in self.data}

        max1=max(d3.values())

        c=[k for k,v in d3.items() if v==max1]

        print(c)

    def automatic(self):

        d4=[r.get("transmission")for r in self.data if r.get("transmission")=="Automatic"]

        #print(d4)

        d3=d4.count("Automatic")

        print(d3)

    def tax(self):

        d3={r.get("model")for r in self.data if r.get("tax")=="260"}

        print(d3)

    def Corolla(self):

        d5=[r.get("model")for r in self.data if r.get("price")=="17498"]

        print(d5)

    def row(self):

        for r in self.data:

            print(self.data[:5])

    

toyotoinstance_1=Toyotta()

#toyotoinstance_1.length()

#toyotoinstance_1.price()

#toyotoinstance_1.transmission()

#toyotoinstance_1.milege()

#toyotoinstance_1.model()

#toyotoinstance_1.automatic()

#toyotoinstance_1.tax()

#toyotoinstance_1.Corolla()

toyotoinstance_1.row()