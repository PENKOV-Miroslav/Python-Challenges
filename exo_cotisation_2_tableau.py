Saisir=int(input("saisir votre age: "))

Tarif=[233, 203, 175, 149, 125, 103, 83]
Age=["Senior","Junior","Cadet","Minime","Benjamin","Poussin","Pousset"]

if Saisir >=21:
    print(" Vous etes ", Age[0],"votre tarif est de ",Tarif[0])
elif (Saisir >=18) and (Saisir <=20):
    print(" Vous etes" ,Age[1] ,"votre tarif est de",Tarif[1])
elif (Saisir >=16)and(Saisir <=17):
    print(" Vous etes",Age[2] ,"votre tarif est de",Tarif[2])
elif (Saisir >=14)and(Saisir <=15):
    print(" Vous etes", Age[3], "votre tarif est de",Tarif[3])
elif (Saisir >=12)and(Saisir <=13):
    print(" Vous etes",Age[4],"votre tarif est de",Tarif[4])
elif (Saisir >=9)and(Saisir <=11):
    print(" Vous etes",Age[5]  ,"votre tarif est de",Tarif[5])
elif (Saisir >=7)and(Saisir <=8):
    print(" Vous etes", Age[6] ," votre tarif est de",Tarif[6])