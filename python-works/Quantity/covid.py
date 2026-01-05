import csv

class Covid:

    data:list

    def __init__(self):

        file_path="python-works\\Quantity\\country_wise_latest_covid.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[row for row in reader]

    def records(self):

        print(len(self.data))

    def death_rate(self):

        death_rate=[r.get("Country/Region")for r in self.data if r.get("Deaths")>"25198"]

        print(death_rate)

    def start(self):

        for r in self.data:

            if r.get("Country/Region").startswith("B"):

                print(r)

    def countries(self):

        countries=[r.get("Country/Region")for r in self.data ]

        print(countries)

    def counting(self):

        count=0

        for r in self.data:

            count+=1

            if r.get("Country/Region").startswith("A"):

                count+=1

        print(count)

    def cases(self):

        cases=[r.get("Country/Region")for r in self.data if r.get("Recovered")> "1000"]

        print(cases)

    def recovered(self):

        recovered={r.get("Country/Region"):r.get("Deaths")for r in self.data}

        max2=max(recovered.values())

        print(max2)

        max1=[k for k,v in recovered.items() if v==max2]

        print(max1)

    

covid_instance=Covid()

#covid_instance.records()

#covid_instance.death_rate()

#covid_instance.start()

#covid_instance.countries()

#covid_instance.counting()

#covid_instance.cases()

covid_instance.recovered()