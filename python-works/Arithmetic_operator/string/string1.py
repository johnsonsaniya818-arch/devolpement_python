
def vowel(word):

    count=0

    vowels="aeiou"

    for ch in word.casefold():

        if ch in vowels:

            count+=1

    return count
    
print(vowel("hello"))

print(vowel("opp"))