g=["Madame","Monsieur"]
p=str(input ("Prénom="))
N=str(input ("Nom="))
l=["direction","secrétariat","gestion","informatique","communication","entretien","fabrication"]
list=str(input("code="))
an="20"+list[0:2]
print(g[int(list[6])-1],p,N,"travaille au service",l[int(list[7])],".Elle/il travaille dans l'entreprise depuis",an,"et son numéro d'embauche est le",list[2:6])