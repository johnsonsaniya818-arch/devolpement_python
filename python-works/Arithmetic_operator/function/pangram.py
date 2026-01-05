
def is_pangram(word):

  word = word.casefold()

  is_pangram = True

  alphabet = "abcdefghijklmnopqrstuvwxyz"

  for ch in alphabet:

    if ch not in word:

      is_pangram = False

      break

  return is_pangram

print(is_pangram("the quick brown fox jumps over lazy dog"))