#SAISIE USER
base=int(input("Saisir la base de conversion : "))
while(base<=1) or (base>36):
    base=int(input("Saisir la base de conversion entre 1 et 36 : "))

n=int(input("Saisir un nombre décimal pour le convertir : "))
while(n<=0):
    n=int(input("Saisir un nombre décimal POSITIF pour le convertir : "))
    
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    
#1ere division
reste = n%base
if (reste>=10):
    reste = alphabet[reste-10]
    
quotient = n/base
quotient = int(quotient) #On garde la partie entiere du quotient
rang=0 #Initialisation du rang

conv=[]
conv.insert(rang,reste)

#Toutes les autres divisions
while (quotient!=0):
    reste = quotient%base
    if (reste>=10):
        reste = alphabet[reste-10]
    
    quotient = quotient/base
    quotient = int(quotient)#On garde la partie entiere du quotient
    rang = rang-1 #On ajoute a chaque fois le reste obtenue dans la liste binaire vers la gauche gauche (soit au rang,rang-1)
    conv.insert(rang,reste)


#Affichage du resultat (pas sous forme de liste)
print(n,"en base",base,"est ",end='')
for i in range (0,len(conv)):
    print(conv[i],end='')