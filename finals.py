def factor(n):
    if n%5 == 0:
        f =  n//5
    elif n%4 == 0:
        f =  n//4
    elif n%3 == 0:
        f =  n//3
    elif n%2 == 0:
        f = n//2
    else:
        return n
    return factor(f)

def middle(n):
    if len(n)== 1:
        return n[0]
    if len(n)==2:
        return n[0]+n[1]
    return middle(n[1:-1])

