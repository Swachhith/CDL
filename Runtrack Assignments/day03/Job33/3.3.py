import re
f = open(r"Job33/data.txt","r")
txt = f.read()
count=0
for match in re.findall(r"[A-Z]?[a-z]+",txt):
    count+=1
print(count)