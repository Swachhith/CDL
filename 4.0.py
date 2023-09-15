def factorial(p):
    if p==0:
        return 0
    elif p ==1:
        return 1
    else:
        return p*factorial(p-1)
print(factorial(5))    