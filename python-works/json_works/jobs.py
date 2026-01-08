from json import load

file_path="python-works\\json_works\\jobs.json"

fr=open(file_path,"r",encoding="utf-8")

data=load(fr)

print(len(data))

for r in data:

    if r.get("title")=="Cloud Engineer":

        print(r.get("id"))
        