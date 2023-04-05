# Un permis de chasse à points remplace désormais le permis de chasse traditionnel. Chaque chasseur possède au départ un capital de 100 points. S'il tue une poule il perd 1 point, 3 points pour 1 chien, 5 points pour une vache et 10 points pour un ami. Le permis coûte 200 euros. Écrire une fonction amende qui reçoit le nombre de victimes du chasseur et qui renvoie la somme due.

#  

# Utilisez cette fonction dans un programme principal qui saisit le nombre de victimes et qui affiche la somme que le chasseur doit débourser.

# victimes = int(input("Entrer le nombre de victimes : "))

chasseurInfos = {   "name" : "nomChasseur", 
                    "capital" : 100, 
                    "cout" : 200,
                     "victimes" : 
                        {"poule" : 1, 
                        "chien" : 3, 
                        "vache" : 5, 
                        "ami" : 10}
                }

chasseurInfos["name"] = input("nom chasseur : ")
poule = int(input("Entrer le nombre des poules : "))
chien = int(input("Entrer le nombre des chiens : "))
vache = int(input("Entrer le nombre des vaches : "))
ami = int(input("Entrer le nombre des amis : "))
# points = 100
# cout = 200

if chasseurInfos["capital"] > 0 : 
    p = poule * chasseurInfos["victimes"]["poule"]
    c = chien * chasseurInfos["victimes"]["chien"]
    v = vache * chasseurInfos["victimes"]["vache"]
    a = ami * chasseurInfos["victimes"]["ami"]
    name = chasseurInfos["name"]
    rslt = p + c + v + a
    print("Le nombre de victimes que vous avez chassée est :", rslt)

    if rslt > chasseurInfos["capital"]:
        print("Vous avez perdu votre permis Mr.", name)
    else: 
        chasseurInfos["capital"] -= rslt
        print("Il faut payer", rslt * 2, "Euro Mr.", name)

