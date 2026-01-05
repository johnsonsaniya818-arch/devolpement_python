
# word1="silent"

# word2="sent"

# is_container_word=True

# for ch in word2:

#     if ch not in word1:

#         is_container_word=False

#         break

# print(is_container_word)

        
word1="silent"

word2="send"

if(set(word2).issuperset(set(word1))):


    print("container word")

else:

    print("not a container word")

