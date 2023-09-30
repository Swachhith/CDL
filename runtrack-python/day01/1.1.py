def draw_rectangle(x,y):
    print("|",end = "")
    for i in range(x-2):
        print("-",end = "")
    print("|")    
    for i in range(y-2):
        print("|",end="")
        for i in range(x-2):
            print(" ",end="")
        print("|",)
        #print("\n")
    print("|",end="")
    for i in range(x-2):
        print("-",end="")
    print("|")  

draw_rectangle(10,5)        