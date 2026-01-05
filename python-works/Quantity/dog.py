import csv

class Dog:

    data:list

    def __init__(self):

        file_path="python-works\\Quantity\\dog_breeds.csv"

        fr=open(file_path,"r",encoding="UTF-8")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

        #print(self.data)

    def records(self):

        print(len(self.data))

    def orgin(self):

        country_breed=[r.get("Breed")for r in self.data if r.get("Country of Origin")=="Canada"]

        print(country_breed)

    def place(self):

        count=0

        for r in self.data:

            if r.get("Country of Origin")=="Germany":

                count+=1

        print(count)

    def longevity(self):
        breeds = [
        r.get("Breed")
        for r in self.data
        if r.get("Longevity (yrs)") == "10-12"
    ]
        print(breeds)

    def character(self):

        character_of_dog=[r.get("Common Health Problems")for r in self.data if r .get("Character Traits")=="Loyal, friendly, intelligent, energetic, good-natured"]

        print(character_of_dog)

    def rows(self):
        for r in self.data[:5]:
            print(r)

    def breed(self):

        for r in self.data:

            print(r.get("Breed"))

    def brown(self):

        brown_eyes={r.get("Character Traits")for r in self.data  if r.get("Color of Eyes")=="Brown"}

        print(brown_eyes)
   



dog_instance=Dog()

#dog_instance.records()

#dog_instance.orgin()

#dog_instance.place()

#dog_instance.longevity()

#dog_instance.character()

#dog_instance.rows()

#dog_instance.breed()

dog_instance.brown()