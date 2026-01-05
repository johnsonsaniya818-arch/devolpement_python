file_path="python-works\\Arithmetic_operator\\Error_handling\\numbers.txt"

try:

    fr=open(file_path,"r")

    li1=[]

    dic={}

    for line in fr:

        line=line.rstrip("\n")

        try:

            num=int(line)

            li1.append(num)

        except Exception as e:

            continue

    print(max(li1))

    print(sum(li1))

    dic={num:li1.count(num)for num in li1}

    print(dic)

    max_count=max(dic.values())

    freq=[k for k,v in dic.items() if v==max_count]

    print(freq)


except Exception as e:

    print(e)


    
