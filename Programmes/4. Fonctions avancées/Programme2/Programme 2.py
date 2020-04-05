from my_fcts import *

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