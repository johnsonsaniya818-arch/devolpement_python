import csv
class food:

    data:str

    def __init__(self):

        file_path="python-works\\Quantity\\indian_food.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

        print(len(self.data))

    def names(self):

        d1=[r for r in self.data if r.get("name")=="Balu shahi"]

        print(d1)

    def veg(self):

        vegeterian=[r for r in self.data if r["diet"] == "vegetarian"]

        print(vegeterian)

    def west_bengal(self):

        west= [r for r in self.data if r.get("state") == "West Bengal"]

        print(west)

    def food(self):

        food_items=[r.get("name") for r in self.data]

        print(food_items)

    def len(self):

        length_of_sweet=len([r for r in self.data if r.get("flavor_profile") == "sweet"])

        print(length_of_sweet)

    def types(self):

        type1=type([r for r in self.data])

        print(type1)

    def time(self):

        time_of_preparation=[r for r in self.data if r.get("prep_time", 0) < "15"]

        print(time_of_preparation)

    def remove(self):

        remove_values=[r for r in self.data if r.get("state") != "-1"]

        print(remove_values)

    def regions(self):

        regions_north=[r for r in self.data if r.get("region") == "North"]

        print(regions_north)

    def flavour(self):

        flavours=[r for r in self.data if r.get("flavor_profile") == "sweet"]

        print(flavours)

    def duplicate(self):

        duplicates=list(set(r.get("name") for r in self.data))

        print(duplicates)














food_instance1=food()

# food_instance1.names()

# food_instance1.veg()

# food_instance1.west_bengal()

# food_instance1.food()

#food_instance1.len()

#food_instance1.types()

#food_instance1.time()

#food_instance1.remove()

#food_instance1.regions()

food_instance1.flavour()

food_instance1.duplicate()



    