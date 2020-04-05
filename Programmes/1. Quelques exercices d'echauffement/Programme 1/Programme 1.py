#SAISIE USER
N=int(input("Choisir le nombre de nombres a colorier : "))

while(N<=0):
    N=int(input("Saisir un nombre de nombres a colorier superieur à 0 : "))


#Initialisation des couleurs
R="\033[31m"
B="\033[34m"


#PROGRAMME
for i in range(1,N+1): #du nombre 1 à N
    if (i%2==0): #si nombre est pair
        print(R,i,end='')
    else : #si nombre est impair
        print(B,i,end='')