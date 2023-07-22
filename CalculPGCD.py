def PGCD(a,b):
    if a%b==0:
        return(b)
    else:
        return(PGCD(b,a%b))