

file_path_sy="Arithmetic_operator\\file\\systemlogs\\systemlog.txt"

file_path_war="Arithmetic_operator\\file\\systemlogs\\warning.txt"

file_path_err="Arithmetic_operator\\file\\systemlogs\\error.txt"

file_path_info="Arithmetic_operator\\file\\systemlogs\\info.txt"

fr_sy=open(file_path_sy,"r")

fr_war=open(file_path_war,"w")

fr_err=open(file_path_err,"w")

fr_info=open(file_path_info,"w")

for line in fr_sy:

    msg=line.rstrip("\n")


    if "ERROR" in msg:

        fr_err.write(msg+"\n")

    elif "WARNING" in msg:

        fr_war.write(msg+"\n")

    elif "INFO" in msg:

         fr_info.write(msg+"\n")


print("program end")


