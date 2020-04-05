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
    while (a in c) : #tant que la couleur est une couleur deja chosie (cad appartenant a c), redemander la couleur
        a = random.choice(color)
    c.insert(i-1,a) #inserer la nouvelle couleur chosie aleatoirement dans color dans c


#Insertion de N valeur (couleur) dans la liste w parmi c
w=c #la liste w a deja n valeur
for cpt in range (n+1,N+1): #de n+1 à N pour que la liste w est N valeur (car elle est initialisé a n valeurs)
    b=random.choice(w)
    w.insert(cpt,b)
random.shuffle(w) #Melanger la liste w pour melanger les trois premiers couleurs de la liste
    
    
#Attribution de chaque valeur de la liste w à chaque Nombre
for j in range(1,N+1):#du nombre 1 à N
    print(w[j-1],j,end='') #j-1 car la liste w commence à l'indice 0 