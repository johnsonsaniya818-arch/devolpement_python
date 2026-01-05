
def consonent(word):

    count=0

    vowels="aeiou"

    for ch in word.casefold():

        if ch not in vowels and ch.isalpha():

            count+=1

    return count

print(consonent("haii"))

        