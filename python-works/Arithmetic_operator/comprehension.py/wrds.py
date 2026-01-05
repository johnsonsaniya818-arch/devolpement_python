
words=["cat","act","madam","hello","malayalam","madam","malayalam","mom"]

w1={}

for w in words:

    if(w==w[::-1]): 
        
        if w not in w1:

            w1[w]=1

        else:

            w1[w]+=1


print(w1)