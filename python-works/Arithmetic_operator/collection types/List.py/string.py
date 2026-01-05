
words = ["hello","hai","hello","is"]

new=[]

new_arr=[]

for word in words:

    if(words.count(word)>1 and word not in new):

        new.append(word)

    elif(word not in new):

        new_arr.append(word)

print(new)

print(new_arr)


