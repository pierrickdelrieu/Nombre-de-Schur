#Donnée
import random

#SAISIE USER
#Nombre de nombres a colorier
N=int(input("Choisir le nombre de nombres a colorier : "))

while(N<=0):
    N=int(input("Saisir un nombre de nombres a colorier superieur à 0 : "))

#Nombre couleur
n=int(input("Choisir un nombre de couleur (entre 1 et 6) : "))

while (n<1) or (n>6) or (n>N):
    n=int(input("Choisir un nombre de couleur (entre 1 et 6) et inferieur au nombre de nombre : "))

print()

#Initialisation de la liste color contenant les couleurs de coloriage
W="\033[0m"       #Noir
R="\033[31m"      #Rouge
G="\033[32m"      #Vert
O="\033[33m"      #Orange
B="\033[34m"      #Bleu
P="\033[35m"      #Violet
color=[W,R,G,O,B,P]

#Création d'une liste aléatoire c avec n couleurs différentes
c=[]
for i in range (1,n+1):
    a=random.choice(color) # choix d'une couleur aléatoire dans color
    c.insert(i-1,a) #inserer la nouvelle couleur chosie aleatoirement dans color dans c

#Test si il y a deux couleurs identiques dans c
test=0 #test=0 si les n couleurs sont presentes
for j in (W,R,G,O,B,P):
    x=c.count(j) #renvoi combien de fois il y a j dans c
    if(x>1):
        test=1 #test=1 si les n couleurs ne sont pas presentes


#Modification de la liste avec N valeurs
for cpt in range (n+1,N+1):
    b=random.choice(c)
    c.insert(cpt,b)

random.shuffle(c) #Melange de la liste c


#Attribution de chaque valeur de la liste c à chaque Nombre et Affichage
print("Pour n =",n,"et N =",N,"le coloriage",end='')
for p in range(0,N):#du nombre 1 à N
    print(c[p],p,end='') #j-1 car la liste w commence à l'indice 0
    

#Affichage si valide ou non
if (test==1):
    print(W," n'est pas valide")
else:
    print(W," est valide")    