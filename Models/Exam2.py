def Somme(mob = list()):
    print("Somme",mob)
    Somme = sum(mob)
    print("La somme est :", Somme)
Somme(mob=(4,5,6))

for x in range(1,101):
    x += x/2
print(x)

M = int(input("Donner la valeur de M :"))
i = 1
for S in range(1,M+1):
    i *= S**5
print(i)


nombre = int(input("Entrez un nombre entier positif : "))
n = 2
for x in range(1,nombre+1):
    n *= x
print(n)
