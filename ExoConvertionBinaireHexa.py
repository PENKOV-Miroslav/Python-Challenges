H = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
B = ["0000","0001","1010","1011","1100","1101","1110","1111"]
rep = str(input("Saisir un noombre binaire: "))
N = str(rep)
n = '0'*(len(rep) % 4)+N
print(rep)
C = ""
for i in range(len(rep)//4):
    for j in range(len(B)):
        if n[4*i:4*i+4] == B[j]:
            C = C+H[B.index(B[j])]
print(rep,"=",C,"en hexadecimal")