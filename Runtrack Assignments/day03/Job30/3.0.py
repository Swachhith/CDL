msg =input("Enter a character string:" )
f = open("output.txt","a")
f.write(msg)
f.close()

f = open("output.txt","r")
print(f.read())