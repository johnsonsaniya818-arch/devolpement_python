import csv

class AiJobs:

    data:list

    def __init__(self):

        file_path="python-works\\Quantity\\AI_Impact_on_Jobs_2030 - Copy.csv"

        fr=open(file_path,"r",encoding="utf-8")

        reader=csv.DictReader(fr)

        self.data=[row for row in reader]

    def records(self):

        print(len(self.data))

    def first_record(self):

        print(self.data[:5])#to print first 5 records using slice

    def exposure(self):

        d1={r.get("Job_Title")
            for r in self.data
            if r.get("Risk_Category")=="High"}
        
        print(d1)

    def experience(self):

        d2={r.get("Job_Title")for r in self.data if r.get("Years_Experience")>"20"}

        print(d2)

    def average(self):

        d3={r.get("Job_Title"):int(r.get("Average_Salary"))for r in self.data}

        print(d3)

        max1=max(d3.values())

        print(max1)

        l1=[k for k,v in d3.items() if v==max1]

        print(l1)

    def education(self):

        li=[r.get("Education_Level")for r in self.data]

        print(li)

    def teacher(self):

        for r in self.data:

            if "Teacher" in r.get("Job_Title"):

                print(r)

    def skill(self):

        d7={r.get("Job_Title")for r in self.data if r.get("Skill_10")=="0.0"}

        print(d7)

    def ai(self):

        d0={r.get("Automation_Probability_2030")for r in self.data if r.get("Job_Title")=="AI Engineer"}

        print(d0)

    def tech_growth(self):

        d8={r.get("Job_Title") for r in self.data if r.get("Tech_Growth_Factor")>"1.0"}

        print(d8)

        


ai_instance1=AiJobs()

ai_instance1.records()

ai_instance1.first_record()

ai_instance1.exposure()

ai_instance1.experience()

ai_instance1.average()

ai_instance1.education()

ai_instance1.teacher()

ai_instance1.skill()

ai_instance1.ai()

ai_instance1.tech_growth()