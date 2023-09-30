def rectangle(h, w):
    for i in range(h):
        if i == 0 or i == h - 1:
            print("|", end="")
            for j in range(w):
                print("-", end="")
            print("|")
        else:
            print("|", end="")
            for j in range(w):
                print(" ", end="")
            print("|")
   