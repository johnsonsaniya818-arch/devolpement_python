
# word="balloon"

# wc={}

# for ch in word:

#     if ch in word and ch not in wc:

#         wc[ch]=1

#     else:

#         print("first occurance",ch)

#         break

def f_recursive(word):

    wc={}

    for ch in word:

        if ch in wc:

            return ch
        
        else:

            wc[ch]=1

    return None

print(f_recursive("python"))

print(f_recursive("balloon"))