def conversion(nb,base,N):
    #1ere division
    reste = nb%base
    quotient = nb/base
    quotient = int(quotient) #On garde la partie entiere du quotient
    rang=0 #Initialisation du rang

    conv=[]
    conv.insert(rang,reste)

    #Toutes les autres divisions
    while (quotient!=0):
        reste = quotient%base
        quotient = quotient/base
        quotient = int(quotient)#On garde la partie entiere du quotient
        rang = rang-1 #On ajoute a chaque fois le reste obtenue dans la liste binaire vers la gauche gauche (soit au rang,rang-1)
        conv.insert(rang,reste)
    
    # On rajoute un 0 en plus pour pouvoir commencer la liste a l'index 1 et pas 0
    if(len(conv)<=N):
        for i in range (0,N-len(conv)+1): 
            conv.insert(0,0)
        
    return (conv)



def combinaison_valide(conv,N):
    
    #LISTE DES TRIPLETS POUR LA COLORATION...
    # détermination des triplets en enlevant les triplets déjà apparu
    a = 1
    b = 1
    triplet_mono=0
    c_valide=0
 
    while (a+b<=N):
        if (a<=b ):        # comme b augmente avant a, on enlève les valeurs de a qui sont plus grandes que b
            #AFFICHAGE DES TRIPLETS
            if (conv[a]==conv[b]) and (conv[a]==conv[a+b]):
                triplet_mono=triplet_mono+1
        if (a+b<N):        # permet d'augmenter la valeur de b en vérifiant que b ne seras pas trop grand
            b = b+1
        else:              # permet d'augmenter a de 1 et de remettre b à 1 quand b est trop grand
            b = 1
            a = a+1
            
    #Compteur de combianison valide 
    if (triplet_mono==0): #Si il y a pas de triplet monochromatique
        c_valide=1
    
    return(c_valide)


def nombre_N_valide(n):
    #Si affichage 1 alors combinaison valide
    #Si affichage 0 alors conbianison pas valide
    #Condition pour que N soit valide    
    if(n!=0): #Si il y a au moin une combinaison valide
        x=1
    else:
        x=0
        
    return (x)


def affichage(n,N):
    #AFFICHAGE FINAL
    print("DONC S(",n,") =",N-1) # valide pour Nmax=N-1 car pour N plus valide
    
    
def intervalle_de_N(n):
    def fact(n):
        x=1
        for i in range(2,n+1):
            x = x*i
        return x

    print("Pour une raison de temps on peut seulement donner un intervalle")
    print("On sait que :",((3**n)-1)/2,"≤ S(",n,") ≤",3*fact(n)-1)
    
    
def saisie_de_n():
    #Saisie de N
    n=int(input("Saisir n ≥ 2 : "))
    while (n<2):
        n=int(input("Saisir n ≥ 2 : "))
    
    if (n>2) and (n<6):
        print("Merci de patienter ... ")
    
    return n

def programme():
    #Initialisation
    N_valide=1
    N=1

    #Saisie de N
    n=int(saisie_de_n())
    print()


    #PROGRAMME POUR n<6
    if (n<6):
        while (N_valide!=0):
            N=N+1
            c_valide=0
            for a in range(0,n**N):       
                conv=conversion(a,n,N)
                c_valide=c_valide + combinaison_valide(conv,N)
            N_valide=nombre_N_valide(c_valide)
        affichage(n,N)

    #PROGRAMME POUR n≥6
    else:
        intervalle_de_N(n)


        
        

    
    
