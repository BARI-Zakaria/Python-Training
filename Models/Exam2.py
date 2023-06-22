import os

# def Somme(mob = list()):
#     print("Somme",mob)
#     Somme = sum(mob)
#     print("La somme est :", Somme)
# Somme(mob=(4,5,6))

# for x in range(1,101):
#     x += x/2
# print(x)

# M = int(input("Donner la valeur de M :"))
# i = 1
# for S in range(1,M+1):
#     i *= S**5
# print(i)


# nombre = int(input("Entrez un nombre entier positif : "))
# n = 2
# for x in range(1,nombre+1):
#     n *= x
# print(n)

    #  GET THE SOMME OF THE SAME EXTENSION FILES SIZE 
Path = r'C:\Users\Zakaria\Desktop\Régional\ExercicesPython'
MyDic = dict()

for dirpath, dirnames, filenames in os.walk(Path):
    for files in filenames:
        split = os.path.splitext(files)[1][1:]
        joinPath = os.path.join(Path, files)
        FileSize = os.path.getsize(joinPath)
        if split in MyDic:
            MyDic[split] += FileSize
        else:
            MyDic[split] = FileSize   
print(MyDic)


