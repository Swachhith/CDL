def rounded(notes):
    for x in range(0, len(notes)):
        if notes[x]>40: 
            if(notes[x] % 5 > 3):
                notes[x] = notes[x] - notes[x]%5 + 5
            # print(notes[x] + ' ')
l = [12, 24, 33, 17, 19, 91, 99]
rounded(l)

for i in l:
    print(i)