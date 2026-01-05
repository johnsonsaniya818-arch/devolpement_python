
def palin(word):

    is_palindrome=True

    word_text=word.casefold()

    word_reverse=word[::-1]

    if word!=word_reverse:

        is_palindrome=False
   
    return is_palindrome

print(palin("malayalam"))

print(palin("seetha"))

