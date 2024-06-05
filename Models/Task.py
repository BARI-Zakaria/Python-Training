# IMPORT THE MODULES NECESSARY

import os
import glob
import shutil

# CREATE AN EMPTY SET AND LIST ALL FILES WITH THE 'GLOB' METHOD

mySet=set()
pathA = r"C:\Users\Zakaria\Desktop\Orientini"
checkList = glob.glob1(pathA, '*.*')
# mySet.update(test)


# EXTRACT THE FILE EXTENSION USING 'SPLIT' METHOD AND ADD IT TO 'MySet'
for files in checkList:
    mySet.add(os.path.splitext(files)[1])

# CREATE A DIRECTORY WITH THE EXTENSION NAME (excluding the dot '.') INSIDE THE 'pathA' DIRECTORY
for exts in mySet:
    direcName = os.path.join(pathA, exts[1:])
    os.makedirs(direcName, exist_ok=True) #exist_ok=True ensures that the directory is created if it doesn't already exist

# THE FILES WITH CURRENT EXTENSION ARE MOVED TO THE CORRECT DIRECTORY
    for dirpath, dirnames, filenames in os.walk(pathA): 
        for exten in filenames:
            extension = os.path.splitext(exten)[1]
            # print(extension)
            if extension == exts:
                sourcePath = os.path.join(dirpath, exten)
                shutil.move(sourcePath, os.path.join(direcName, exten))
                # print(extension)
