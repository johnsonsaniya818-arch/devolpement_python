
def anagram(word1,word2):

    is_anagram=True

    if len(word1)!=len(word2):

        return False

    for ch in word1:

        ch_in_count_w1=word1.count(ch)

        ch_in_count_w2=word2.count(ch)

        if ch_in_count_w1!=ch_in_count_w2:

            is_anagram=False

            break
   
    return is_anagram

print(anagram("cat","acts"))

print(anagram("amma","apple"))
    