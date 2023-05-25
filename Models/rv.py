import os
import glob
import shutil


mySet=set()
pathA = "C:\\Users\\Zakaria\\Desktop\\BB"
test = glob.glob1(pathA, '*.*')
# print(test)

mySet.update(test)
print(mySet)

for dirpath, dirnames, filenames in os.walk(pathA):
    for exten in filenames:
        # if exten == ""
        extenstion = os.path.splitext(exten)[1]
        if extenstion in mySet:
            shutil.copyfile()