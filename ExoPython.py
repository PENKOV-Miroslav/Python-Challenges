#On importe la librairie random qui contient la fonction randint
from random import randint

#Stocke le montant des gains
gain = 0
#On prend un tableau dans lequel on a 5 nombres au hasard
T=[randint(1,5) for i in range (5)]
print(T)
for i in range (1,6):
    #Si le même nombre apparaît 3 fois ou plus, l’utilisateur gagne 5 euros
    a=T.count(i)
    if a>=3:
        gain = gain+5
        print("L'utilisateur a gagne 5 euros car il y a au moins un nombre en double")
#On additionne ces nombres
sum(T)

#Si la somme des nombres est paire, l’utilisateur gagne 1 euro
if sum(T) % 2 == 0:
  gain += 1
  print("L'utilisateur a gagne 1 euro grâce a une somme de nombres paires")

#Si le plus grand nombre est 2, alors l’utilisateur gagne 2 euros
if max(T) == 2:
  gain += 2
  print("L'utilisateur a gagne 2 euros car le plus grand nombre est 2")

#Si le gain est superieur a 0
if gain !=0:
  print("L'utilisateur a gagne au total " + str(gain) + " euro")
else: #Si le gain est nulle
  print("L'utilisateur n'a rien gagne")