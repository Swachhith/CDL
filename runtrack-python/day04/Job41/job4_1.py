def power(x,n):
    if n==0 :
        return 1
    if n==1:
        return x
    else:
        return x*power(x,n-1)

x=int(input("enter a whole nummber:"))
n=int(input("enter the power in the whole number:"))
print(power(x,n))
