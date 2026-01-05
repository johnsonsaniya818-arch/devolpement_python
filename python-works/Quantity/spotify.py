file_path="python-works\\Quantity\\spotify_data clean.csv"

fr=open(file_path,"r",encoding="UTF-8")

import csv

reader=csv.DictReader(fr)

data=[row for row in reader]

dic1={}

for r in data:

    album=r.get("album_name")

    duration=r.get("track_duration_min")

    if album not in dic1:

        dic1[album]=duration

max1=max(dic1.values())

print(max1)

li1=[k for k,v in dic1.items()if v==max1]

print(li1)




    

    