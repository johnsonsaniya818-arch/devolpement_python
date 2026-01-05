
word="abcdcdbaabcd"

slicing="aa"

count=0

for i in range(0,11):

    sliced_word=word[i:i+2]

    if slicing==sliced_word:

        count+=1

print(count)

