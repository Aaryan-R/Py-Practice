def solve(word):
   char_list = []
   for char in word:
      if char.isalpha():
         if char in char_list:
            return False
            char_list.append(char)
   return True
s = "python"
print(solve(s))