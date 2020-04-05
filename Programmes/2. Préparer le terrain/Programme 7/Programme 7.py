#SAISIE USER
n=int(input("Saisir un nombre décimal pour le convertir en binaire : "))
while(n<=0):
    n=int(input("Saisir un nombre décimal POSITIF pour le convertir en binaire : "))


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


print(n,"-->",binaire)












