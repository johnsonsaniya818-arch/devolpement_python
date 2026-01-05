
file_path="C:\\Users\\Lenovo\\Desktop\\devolpment-journey\\python-works\\Arithmetic_operator\\file\\wrds.py"

fr=open(file_path,"r")

st=[]

for line in fr:

    line=line.rstrip("\n")

    if line==line[::-1]:

        st.append(line)

print(st)

