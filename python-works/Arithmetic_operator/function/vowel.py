
def vowels_consonants_count(word):

  v_count = 0

  c_count = 0

  vowels = "aeiou"

  for ch in word.casefold():

    if ch in vowels:

      v_count+=1

    elif ch.isalpha():

      c_count+=1

  print("vowel count =",v_count)

  print("consonants count=",c_count)

vowels_consonants_count("hello123")