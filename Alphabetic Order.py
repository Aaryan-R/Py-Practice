my_str = "The quick brown fox jumps over the lazy dog"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")
for word in words:
   print(word)
