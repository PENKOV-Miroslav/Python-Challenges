def somme(n):
    if n==1:
        return(1)
    else:
        return(somme(n-1)+n)