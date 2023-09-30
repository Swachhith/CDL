import re
f = open(r"Job32/domains.xml","r")
txt = f.read()
count=0
for match in re.findall(r"\.([a-z].?){2,20}\.?([a-z]{2,6})?",txt):
    count+=1
print(count)    