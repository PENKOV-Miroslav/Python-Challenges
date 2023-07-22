N=int(input("Saisir le nombre de note:"))

T=[]
for i in range (N):
    T.append(float(input()))
print(T)

moyenne=sum(T)/N
print("La moyen est de",moyenne)
print("La note maximale est:",max(T))
print("La note minimale est de",min(T))
print("L'etendu est de",max(T)-min(T))

c=0
if T[1]==10:
    c=c+1
    print("Le nombre de notes en dessous de 10 :",c)

n=sorted(T) #classe les nombre dans l'ordre croissant.
Me=(n[int(N/2)-1]+n[int(N/2)])/2
print("La médiane est de:",Me)
M=((sum(T)-min(T)-max(T)))/28
print("La moyenne élaguée est de:",M)

# intervertir des chiffre T=[T[0]]
#T[i];T[i+1]=T[i+1];T[i]