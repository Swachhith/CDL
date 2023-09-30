def in_desc_order(str) :
    n = len(str)
    b = True
    for i in range(n-1) :
        b = b and str[i]>str[i+1]
    return(b)

def order_str(str) :
    res = str
    n = len(str)
    for i in range(n, 0, -1) :
        for j in range(i-1) :
            if res[j]>res[j+1] :
                res = res[:j]+res[j+1]+res[j]+res[j+2:]
    return(res)

def next(str) :
    n = len(str)
    for i in range(2,n+1) :
        end = str[-i:]
        if (not in_desc_order(end)) :
            end = end[1]+order_str(end[0]+end[2:])
            return(str[:-i]+end)
    return(str)

next("abcde")