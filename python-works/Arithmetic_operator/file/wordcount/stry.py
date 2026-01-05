
file_path_stry="Arithmetic_operator\\file\\wordcount\\stry.txt"

fr_file_path_stry=open(file_path_stry,"r")

wrd_c={}

for line in fr_file_path_stry:

    line=line.rstrip("\n")

    words=line.split(" ")

    for w in words:

        w=w.rstrip(".")

        w=w.rstrip(",")

        if w not in wrd_c:

            wrd_c[w]=1

        else:

            wrd_c[w]+=1

max1=max(wrd_c.values())

print(max1)

li1=[k for k,v in wrd_c.items() if max1== v and k.isalpha()]

print(li1)

   