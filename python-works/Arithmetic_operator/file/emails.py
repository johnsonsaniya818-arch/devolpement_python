
file_path_email="Arithmetic_operator\\file\\email.txt"

file_path_gmail="Arithmetic_operator\\file\\gmail.txt"

file_path_yahoo="Arithmetic_operator\\file\\yahoo.txt"

file_path_outlook="Arithmetic_operator\\file\\outlook.txt"

fr_email=open(file_path_email,"r")

fw_gmail=open(file_path_gmail,"w")

fw_yahoo=open(file_path_yahoo,"w")

fw_outlook=open(file_path_outlook,"w")

for line in fr_email:

    email=line.rstrip("\n")

    if email.endswith("gmail.com"):

        fw_gmail.write(email+"\n")

    elif email.endswith("yahoo.com"):

        fw_yahoo.write(email+"\n")

    elif email.endswith("out_look.com"):

        fw_outlook.write(email+"\n")

print("end program")

