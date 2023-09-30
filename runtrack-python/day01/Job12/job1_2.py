def print_triangle(h):
    for i in range(h):
        for j in range(h - i - 1):
            print(" ", end='')
        
        print("/", end='')
        
        for j in range(2 * i):
            print(" ", end='')
        
        print("\\")
    
    for i in range(2 * h):
        print("_", end='')
    
    print("")  

