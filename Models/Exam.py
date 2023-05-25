import os
import glob
import shutil


mySet=set()
pathA = "C:\\Users\\Zakaria\\Desktop\\Régional"
checkList = glob.glob1(pathA, '*.*')
# mySet.update(test)

for files in checkList:
    mySet.add(os.path.splitext(files)[1])

for exts in mySet:
    direcName = os.path.join(pathA, exts[1:])
    os.makedirs(direcName, exist_ok=True)

    for dirpath, dirnames, filenames in os.walk(pathA):
        for exten in filenames:
            extension = os.path.splitext(exten)[1]
            # print(extension)
            if extension == exts:
                sourcePath = os.path.join(dirpath, exten)
                # destiPath = os.path.join(destiDirec, exten)
                shutil.move(sourcePath, os.path.join(direcName, exten))
                # print(extension)
            else:
                print("No files to move!!")
                break

