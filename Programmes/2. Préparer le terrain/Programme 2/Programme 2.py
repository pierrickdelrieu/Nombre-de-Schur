# détermination de la valeur maximale de a+b

p = int(input("Entrer un nombre en 2 et 100 : "))
while(p<2 or p>100):
    p = int(input("Entrer un nombre en 2 et 100 : "))


# détermination des triplets en enlevant les triplets déjà apparu

a = 1
b = 1
while (a+b<=p):
    if (a<=b ):        # comme b augmente avant a, on enlève les valeurs de a qui sont plus grandes que b
        print("(",a,",",b,",",a+b,")")
    if (a+b<p):        # permet d'augmenter la valeur de b en vérifiant que b ne seras pas trop grand
        b = b+1
    else:              # permet d'augmenter a de 1 et de remettre b à 1 quand b est trop grand
        b = 1
        a = a+1
        
