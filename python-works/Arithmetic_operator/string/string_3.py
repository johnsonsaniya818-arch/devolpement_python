
def pangram(text):

    ALPHABETS="abcdefghijklmnopqrstuvwxyz"

    is_pangram=True

    for al in ALPHABETS:

        if al not in text.casefold(
            
        ):

            is_pangram=False

            break
    
    return is_pangram

print(pangram("hello"))

print(pangram("THE QUICK BROWN FOX JUMPS OVER LAZY DOG"))