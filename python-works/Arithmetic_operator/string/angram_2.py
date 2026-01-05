
def anagram(word1,word2):

    str_wrd1=sorted(word1)

    str_wrd2=sorted(word2)

    return str_wrd1==str_wrd2

print(anagram("cat","act"))

print(anagram("man","war"))