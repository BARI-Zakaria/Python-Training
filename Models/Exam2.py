import os
import subprocess
import random
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

    # SUBPROCESS DISPLAY RESULT OF A COMMAND LINE WINDOWS WICH IS NOT BUILD IN PYHTON§§
SkutLeMok = subprocess.run("ipconfig", shell=True, text=True, capture_output=True)
# print(SkutLeMok.stderr)
print(SkutLeMok.stdout)

# LET T BE AN ARRAY OF TWENTY RANDOM ELEMENTS OF WHOLE TYPES. WRITE THE PROGRAM THAT ALLOWS TO CALCULATE THE SUM OF THE ELEMENTS OF THIS TABLE. THEN WRITE THE ALGORITHM THAT DETERMINES THE LARGEST, SMALLEST AND SUM OF THIS ARRAY.

T = []
for i in range(20):
    T.append(random.randint(1,100))
somme = sum(T)
somme1 = sum(T)/len(T)
maximum = max(T)
minimum = min(T)
print(T)
print("Le minimum est :", minimum)
print("Le maximum est :", maximum)
print("La somme est :", somme)
print("La somme 2 est :", somme1)


