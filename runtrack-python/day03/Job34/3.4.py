import re
f =open(r"Job33/data.txt","r")
txt = f.read()
x = input("Please wnter a whole number: ")
r1 = "\s[a-zA-z]{" +x+"}\s"
count =0
for match in re.findall(r1,txt):
    count+=1
      
print(f"The number of words with {x} letters are {count}")