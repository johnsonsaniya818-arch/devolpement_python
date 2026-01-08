from json import load

file_path="python-works\\json_works\\process_student.json"

fr=open(file_path,"r",encoding="utf-8")

data=load(fr)#convert json => python native type

result=[st.get("name")for st in data if st.get("course")=="testing"]

print(result)