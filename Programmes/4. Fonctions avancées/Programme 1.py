def fact(n):
    x=1
    for i in range(2,n+1):
        x = x*i
    return x

n=int(input("Saisir une entier n ≥ 6 : "))
while(n<6):
    n=int(input("Saisir une entier n ≥ 6 : "))

print("On sait que :",((3**n)-1)/2,"≤ S(",n,") ≤",3*fact(n)-1)
print()