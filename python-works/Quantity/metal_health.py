import csv

class MentalHealth:

    data:str

    def __init__(self):

        file_path="python-works\\Quantity\\mental_health_social_media_dataset.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

    def length(self):

        print(len(self.data))

    def platform(self):

        d3=[r.get("person_name")for r in self.data if r.get("platform")=="Instagram"]

        print(d3)

    def age(self):

        d4=[r.get("person_name")for r in self.data if r.get("age")>"30"]

        print(d4)

    def counting(self):

        count=0

        for r in self.data:

            if r.get("gender")=="Male":

                count+=1

        print(count)

    def female(self):

        count=0

        for r in self.data:

            if r.get("platform")=="Snapchat":

                if r.get("gender")=="Female":

                    count+=1

        print(count)

    def row(self):

       d3=self.data[:4]

       print(d3)

    def screen(self):

        d4 = [
        r.get("person_name")
        for r in self.data
        if int(r.get("positive_interactions_count")) > 5
    ]
        print(d4)

    def s(self):

        d3=[r.get("person_name")for r in self.data if r.get("daily_screen_time_min")=="390"]

        print(d3)

    def maximum(self):

        d4={r.get("person_name"):r.get("negative_interactions_count")for r in self.data}

        max1=max(d4.values())

        e=[k for k,v in d4.items() if v== max1]

        print(e)

    def person(self):

        d4={r.get("person_name"):r.get("age")for r in self.data}

        print(d4)

    def sleep(self):

        d3=[r for r in self.data if r.get("sleep_hours")>"1.0"]

        print(d3)

methal_healthinstance1=MentalHealth()

methal_healthinstance1.length()

methal_healthinstance1.platform()

methal_healthinstance1.age()

methal_healthinstance1.counting()

methal_healthinstance1.female()

methal_healthinstance1.row()

methal_healthinstance1.screen()

methal_healthinstance1.s()

methal_healthinstance1.maximum()

methal_healthinstance1.person()

methal_healthinstance1.sleep()