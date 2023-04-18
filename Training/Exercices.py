    # 5. Ecrire un algorithme qui permet de calculer le périmètre et la surface d’un rectangle ?

L = float(input("Entrer la longueur du rectangle : "))
l = float(input("Entrer la largeur du rectangle : "))
Surf = L*l 
Perim = (L+l)*2
print("La surface du rectangle est :", Surf)
print("Le périmétre du rectangle est :", Perim)

    # 6. Ecrire un algorithme permettant d’échanger les valeurs de deux variables A et B, et ce quel que soit leur contenu préalable. 

A = int(input("Entrer la valeur de A : "))
B = int(input("Entrer la valeur de B : "))
C = B
B = A 
A = C
print("La valeur de A sera :", A)
print("La valeur de B sera :", B)

    # 7. Ecrire un algorithme qui permet de faire la permutation entre trois nombres entiers ?

X = int(input("Entrer la valeur de X : "))
Y = int(input("Entrer la valeur de Y : "))
Z = int(input("Entrer la valeur de Z : "))

print("Valeurs initiales : X =", X, ", Y =", Y, ", Z =", Z)

temp = X
X = Y
Y = temp

temp = Y
Y = Z
Z = temp

print("Nouvelles valeurs : X =", X, ", Y =", Y, ", Z =", Z)


#     # 8. A la fin d’année, pour chaque étudiant doit avoir deux notes : note écrite (ne) de coefficient 5 et noteorale (no) de coefficient 3. Ecrire un algorithme qui permet de calculer la moyenne et d’afficher l’un des résultats suivantes : « Admis » ou « Echoué »

NEcrite = float(input("Entrer la note écrite :"))*5
NOrale = float(input("Entrer la note orale :"))*3
Moyenne = (NEcrite + NOrale)/2

if Moyenne < 10:
    print("Echoué")
else:
    print("Admis")


    # 9. Un magasin dispose de cinq produits :

ProdA = 5.00
ProdB = 2.50
ProdC = 3.00
ProdD = 10.00
ProdE = 7.00

X = int(input("Combien de X unités du produit A : "))*ProdA
Y = int(input("Combien de Y unités du produit B : "))*ProdB
Z = int(input("Combien de Z unités du produit C : "))*ProdC
T = int(input("Combien de T unités du produit D : "))*ProdD
U = int(input("Combien de U unités du produit E : "))*ProdE

ttva = 0.20

pht = (ProdA*X) + (ProdB*Y) + (ProdC*Z) + (ProdD*T) + (ProdE*U)

tva = pht * ttva

pttc = pht * tva 

print("Le prix hors taxe (PHT) est : ", pht)
print("Le taxe sur la valeur ajoutée (TVA) est : ", tva)
print("Le prix toutes taxes comprises (PTTC) est : ", pttc)

    # 10. Ecrire un algorithme qui permet de calculer la somme a payé (sp). 

Q = int(input("Combien de quantités de bouteilles : "))
pu = float(input("Le prix unitaire : "))
tc = Q * pu
trans = tc * 0.10
sp = trans + tc

print("Le total de la commande est : ", tc)

if tc > 500:
    print("Le transport est gratuit!!")
else:
    print("Tu doit ajouter 10% ""de TC pour le transport, dont la somme a payé sera : ", sp)


    # 11. Écrire un algorithme qui lit deux valeurs entières (A et B) au clavier et qui affiche le signe de la somme de A et B sans faire l'addition. 

A = int(input("Entrez la valeur de A : "))
B = int(input("Entrez la valeur de B : "))

if A >= 0 and B >= 0:
    print("La somme de A et B est positive")
elif A < 0 and B < 0:
    print("La somme de A et B est négative")
else:
    print("La somme de A et B est nulle")


    # 12. Écrire un algorithme qui affiche la valeur absolue d’un nombre 
    
number = float(input("Entrer un nombre : "))

if number < 0:
    print("La valeur absolu du nombre", number, "est : ", -number)
else:
    print("La valeur absolu du nombre", number, "est : ", number)

    # 13. Écrire un algorithme qui permet la résolution d’une équation du premier degré (une équation  sous la forme ax+b=0) 
a = float(input("Entrez la valeur de a : "))
b = float(input("Entrez la valeur de b : "))

if a == 0:
    if b == 0:
        print("L'équation a une infinité de solutions")
    else:
        print("L'équation n'a pas de solution")
else:
    x = -b/a
    print("La solution de l'équation est x =", x)

    # 15.Ecrire un a lgorithme qui range trois nombres donné x, y, z, dans l'ordre croissant (x < y < z). 

x = float(input("Entrez la valeur de x : "))
y = float(input("Entrez la valeur de y : "))
z = float(input("Entrez la valeur de z : "))

if x > y:
    x, y = y, x
if y > z:
    y, z = z, y
if x > y:
    x, y = y, x

print("Les nombres dans l'ordre croissant sont :", x, y, z)
