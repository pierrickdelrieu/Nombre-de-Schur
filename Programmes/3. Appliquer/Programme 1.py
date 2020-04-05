N=1
#0 = rouge
#1 = bleu
N_valide=1

 
 
#PROGRAMME
while (N_valide==1):
    N=N+1
    c_valide=0
    for n in range(0,2**N):
       
        #COLORATION ...
        #1ere division
        reste = n%2
        quotient = n/2
        quotient = int(quotient) #On garde la partie entiere du quotient
        rang=0 #Initialisation du rang
 
        binaire=[]
        binaire.insert(rang,reste)
 
        #Toutes les autres divisions
        while (quotient!=0):
            reste = quotient%2
            quotient = quotient/2
            quotient = int(quotient)#On garde la partie entiere du quotient
            rang = rang-1 #On ajoute a chaque fois le reste obtenue dans la liste binaire vers la gauche gauche (soit au rang,rang-1)
            binaire.insert(rang,reste)
        print(binaire)

        if(len(binaire)<=N):#creation d'une liste de taille N en rajoutant des 0 a gauche
            for i in range (0,N-len(binaire)+1): # On rajoute un 0 en plus pour pouvoir commencer la liste a l'index 1 et pas 0
#Sinon on obtient apres lors de la realisation des triplets une sortie de la liste lors de la comparaison avec binaire[a+b]
                binaire.insert(0,0)
   
   

        #LISTE DES TRIPLETS POUR LA COLORATION...
        # détermination des triplets en enlevant les triplets déjà apparu
        a = 1
        b = 1
        triplet_mono=0

        while (a+b<=N+1):
            if (a<=b ):        # comme b augmente avant a, on enlève les valeurs de a qui sont plus grandes que b
                print("(",binaire[a],",",binaire[b],",",binaire[a+b],")")
                if (binaire[a]==binaire[b]) and (binaire[a]==binaire[a+b]):
                    triplet_mono=triplet_mono+1
            if (a+b<N):        # permet d'augmenter la valeur de b en vérifiant que b ne seras pas trop grand
                b = b+1
            else:              # permet d'augmenter a de 1 et de remettre b à 1 quand b est trop grand
                b = 1
                a = a+1
        print()
   
        #Compteur de combianison valide 
        if (triplet_mono==0): #Si il y a pas de triplet monochromatique
            c_valide=c_valide+1
            
        print()
            
        
    #Condition pour que N soit valide    
    if(c_valide!=0): #Si il y a au moin une combinaison valide
        N_valide=1
    else:
        N_valide=0
            
       
 

#AFFICHAGE FINAL
print("DONC S(2) =",N-1) # valide pour Nmax=N-1 car pour N plus valide