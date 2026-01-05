
s1="python"

s2="typhon"

sorted_1=sorted(s1)

sorted_2=sorted(s2)

if(set(sorted_1)==set(sorted_2)):

    print("anagram")

else:

    print("not a anagram")

print(type(sorted_1))