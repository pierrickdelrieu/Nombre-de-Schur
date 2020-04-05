#SAISIE USER
#Nombre de nombres a colorier
N=int(input("Choisir le nombre de nombres a colorier : "))

while(N<=0):
    N=int(input("Saisir un nombre de nombres a colorier superieur à 0 : "))

#Nombre couleur
n=int(input("Choisir un nombre de couleur (entre 1 et 6) : "))

while (n<1) or (n>6) or (n>N):
    n=int(input("Choisir un nombre de couleur (entre 1 et 6) et inferieur au nombre de nombre : "))


#Initialisation
liste=[]
nb_cb=0 #compteur du nombre de combinaison valide



#PROGRAMME
for a in range(0,n**N):       
    #COLORATION ...  Ici base = N  
    #1ere division
    reste = a%n
    quotient = a/n
    quotient = int(quotient) #On garde la partie entiere du quotient
    rang=0 #Initialisation du rang

    conv=[]
    conv.insert(rang,reste)

    #Toutes les autres divisions
    while (quotient!=0):
        reste = quotient%n
        quotient = quotient/n
        quotient = int(quotient)#On garde la partie entiere du quotient
        rang = rang-1 #On ajoute a chaque fois le reste obtenue dans la liste binaire vers la gauche gauche (soit au rang,rang-1)
        conv.insert(rang,reste)
        
        
    # On rajoute un 0 vers la gauche pour pouvoir avoir une liste de taille N
    if(len(conv)<=N):
        for i in range (0,N-len(conv)): 
            conv.insert(0,0)
            
            
    #Insertion dans une liste seulement les combinaisons qui contiennent les n couleurs
    valide=0 #Initialisation de la variable valide (0 si cb valide et 1 sinon)       
    for i in range (0,n): #Pour n couleurs qui doivent apparaitre
        a=conv.count(i) #on regarde combien de fois la couleur est dans la liste conv
        if (a==0): #Si la couleur est 0 fois dans la liste conv
            valide=1 #alors la combinaisons n'est pas valide
    
    if (valide==0): # si la combinaison est valide
        #Insertion de la combinaison dans une liste
        liste.append(conv) #utilisation de append pour inserer une liste dans une liste
        nb_cb=nb_cb+1



#AFFICHAGE
print()
print("Il y a :",nb_cb,"combinaisons.")
print ("Les combinaisons sont :",liste)
    
    
    