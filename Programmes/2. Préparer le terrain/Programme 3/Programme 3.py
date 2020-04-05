# Donnée
import random

# initialisation d'une liste contenant les couleurs à utiliser
W = "\033[0m"           # noir
R = "\033[31m"          # rouge
B = "\033[34m"          # bleu
color = [R, B]

#Saisie User
#Nombre de nombres à colorier
N = int(input("Entrer un nombre en 2 et 100: "))
while(N<2 or N>100):
    N = int(input("Entrer un nombre en 2 et 100"))

#Création d'une liste aléatoire c avec 2 couleurs différentes et N valeurs
cn = []
for i in range (0,N):
    a = (random.choice(color))
    cn.append(a)
    print(a,i+1,end='') #Affichage des N couleurs colorier avec 2 couleurs
print(W,"")#Pour ne pas afficher la parenthese d'apres en couleur et afficher les triplets a la ligne


#Toutes les combinaisons possibles
nb1 = 1 #initialisation nb1 
nb2 = 1 #initialisation nb1
cpt=0 #Initialisation cpt : si cpt=0 alors pas de triplet monochromatique
while (nb1+nb2<=N): #Toutes les combinaisons jusqu'a nb1+nb2<=N
#Prints de toute les combinaisons ou le nombre 1 est inferieur au nombre 2    
    if (nb1<=nb2):  
        print("(",cn[nb1-1],nb1,W,",",cn[nb2-1],nb2,W,",",cn[nb1+nb2-1],nb1+nb2,W,")")
        if (cn[nb1-1] == cn[nb2-1]) and (cn[nb1-1] == cn[nb1+nb2-1]): #si toutes les couleurs sont identiques 
            cpt = 1 

    if (nb1+nb2<N): 
        nb2 = nb2+1
    #Si toute les combinaisons avec nb1+nb2<N on etait faites alors au augment le nombre 1   
    else:     
        nb2 = 1 #on reinitialise le nombre 2
        nb1 = nb1+1
        

#Affichage de vraie ou faux
if (cpt==1):
    print("Il y a au moin un triplet qui est monochromatique (FAUX)")
else:
    print("Il n'y a pas de triplet monochromatique (VRAIE)")
    