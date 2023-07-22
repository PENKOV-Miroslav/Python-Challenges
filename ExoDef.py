def ldiv(n,v):
    L=[]
    V=[]
    N=[]
    for i in range(1,n+1):
           if n%i==0:
            L.append(i)


    for i in range(1,v+1):
               if v%i==0:
                V.append(i)


    for i in range (len(V)):
        for j in range (len(L)):
            if V[i]==L[j]:
                N.append (V[i])

    return[N, N[-1]]