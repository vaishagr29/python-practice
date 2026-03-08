def add(n1,n2):
    return n1+n2
def substraction(n1,n2):
    if(n1<n2):
        n1,n2=n2,n1
        return n1-n2
    else:
        return n1-n2

def div(n1,n2):
    if(n2==0):
        return f"cannot divide by zero"
    else:
        return n1/n2

def product(n1,n2):
    return n1*n2
