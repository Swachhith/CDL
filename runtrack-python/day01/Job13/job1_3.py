def score(s):
    i=len(s)
    for j in range(0,i):
        if s[j]>40:
            if s[j]%10==3 or s[j]%10==8:
                s[j]=s[j]+2
            elif s[j]%10==4 or s[j]%10==9:
                s[j]=s[j]+1
    print(s)
    
s=[38,39,40,43]
score(s)