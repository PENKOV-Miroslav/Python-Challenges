h=str(input("Saisir un nobre entier écrit en base hexadécimale : "))
print("En décimale le resultat est de :")
print(int(h,16))

#-----------------------------------------------------------

h = "0123456789ABCDEF"
rep = str(input("Saisir un nobre entier écrit en base hexadécimale : "))
s=0
for i in range(len(rep)):
    for j in range(16):
        if rep[i]==h[j] and j<=9:
            s=int(rep[i])*16**(len(rep)-i-1)+s
        if rep[i]==h[j] and j>=10:
            s=j*16**(len(rep)-i-1)+s
print(rep,"en décimale cella donne :",s)