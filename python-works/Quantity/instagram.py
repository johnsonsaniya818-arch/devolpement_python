import csv

class Instagram:

    data:list

    def __init__(self):
        
        file_path="python-works\\Quantity\\Instagram_Analytics.csv"

        fr=open(file_path,"r")

        reader=csv.DictReader(fr)

        self.data=[r for r in reader]

    def length(self):

        print(len(self.data))

    def post(self):

        d1=[r for r in self.data if r.get("post_id")=="IG0000003"]

        print(d1)

    def reels(self):

        d1=[r for r in self.data if r.get("media_type")=="Reel"]

        print(d1)

    def rows(self):


        d4=self.data[:5]

        print(d4)

    def reach(self):

        d5=[r.get("post_id")for r in self.data if r.get("reach")>"2000"]

        print(d5)
    
    def followers(self):

        d4=[r for r in self.data if r.get("followers_gained")=="899"]

        print(d4)

    def like(self):

        d3={r.get("post_id"):r.get("likes")for r in self.data }

        max1=max(d3.values())

        d0=[k for k,v in d3.items() if v==max1]

        print(d0)

    def gained(self):

        d4={r.get("engagement_rate"):r.get("post_id") for r in self.data}

        print(d4)
    def hash(self):

        d2={r.get("post_id"):r.get("hashtags_count")for r in self.data}

        min1=min(d2.values())

        e=[k for k,v in d2.items() if v==min1]

        print(e)
       
instagram_instance1=Instagram()

#instagram_instance1.length()

# instagram_instance1.post()

#instagram_instance1.reels()

#instagram_instance1.rows()

#instagram_instance1.reach()

#instagram_instance1.followers()

#instagram_instance1.like()

#instagram_instance1.gained()

instagram_instance1.hash()

