def with_rec(n) :
    if n < 0:
        return "please Enter number which is greater than 0..."
    else :
        if (n==1 or n==0) :
            return 1 
        else :
            return n * with_rec(n - 1)

def without_rec(n):
    if n < 0:
        return "please Enter number which is greater than 0..."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact