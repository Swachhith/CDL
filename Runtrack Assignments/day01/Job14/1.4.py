import string
x = input("Please enter a word with only alphabets : ")
if x.isalpha():
    if x.islower():
        letters = list(x)
        for i in range(len(letters)-1):
          if string.ascii_lowercase.index(letters[len(letters)-i]) > string.ascii_lowercase.index(letters[len(letters)-i-1]):
             y = letters[len(letters)-i]
             letters[len(letters)-i]=letters[len(letters)-i-1]
             letters[len(letters)-i-1] = y
        print(letters)                                                                      