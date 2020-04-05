# Donnée
import random     #fonction permettant de choisir aléatoirement une valeur dans une liste

#Saisie user
i=int(input("Saisir un nombre i pour definir l'intervalle [1;i] pour les deux premiers elements de la liste (car c=a+b): "))
while (i<1):
    i=int(input("Saisir un nombre i pour definir l'intervalle [1;i] pour les deux premiers elements de la liste (car c=a+b: "))


# initialisation d'une liste contenant les couleurs à utiliser
W = "\033[0m"           # noir
R = "\033[31m"          # rouge
G = "\033[32m"          # vert
O = "\033[33m"          # orange
B = "\033[34m"          # bleu
P = "\033[35m"          # violet
color = [W, R, G, O, B, P]  


# création d'une liste de nombre de 1 à i qui seront pris pour faire les triplets
nombre = [j for j in range (1,i+1)] 


#initialisation des valeurs du triplet et des couleurs des nombres
c1 = (random.choice(color))     #couleur du premier nombre
c2 = (random.choice(color))     #couleur du deuxiéme nombre
c3 = (random.choice(color))     #couleur du troisième nombre
n1 = (random.choice(nombre))       #valeur du premier nombre
n2 = (random.choice(nombre))       #valeur du deuxième nombre
n3 = (n1+n2)                       #le troisiéme nomre est égal à la somme des deux premiers


#détermination de la monochromie du triplet
if (c1==c2) and (c1==c3):     #si les couleurs sont les mêmes
    print("ce triplet (",c1, n1,W,",",c2, n2,W,",",c3, n3,W,") est monochromatique")
else :                      #si les couleurs sont différentes
    print("ce triplet (",c1, n1,W,",",c2, n2,W,",",c3, n3,W,") n'est pas monochromatique")
    
#on rajoute les W pour recolorier les virgules et la fin du texte