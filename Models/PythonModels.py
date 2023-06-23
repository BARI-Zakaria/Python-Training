import os
from datetime import datetime
import glob
        #   TO GET YOUR LOCAL LOCATION
print(os.getcwd())

        #    TO CHANGE YOUR LOCATION
patH = "C:\\Users\\Zakaria\\Desktop\\Python\\PythonModels"
os.chdir(patH)

paTH = "C:\\Users\\Zakaria\\Desktop\\Python"

        #   TO LIST THE CONTENT INSIDE A DIRECTORY
print(os.listdir())

        #   TO MAKE/CREATE A DIRECTORY OR MAKE/CREATE A DIRECTORY WITH SUB-DIRECTORY
os.mkdir('Models')
os.makedirs('Models1/OSModel/MMM')

        #   TO REMOVE A DIRECTORY OR REMOVE A DIRECTORY WITH SUB-DIRECTORY

os.rmdir('Models1/OSModel/MMM')
os.removedirs('Models1/OSModel')

        #   TO RENAME A FILE/DIRECTORY

os.rename("Models", "PythonModels")

        #   TO GET STATS/DETAILS OF A FILE

print(os.stat('osModel.py')) #GENERALLY
print(os.stat('osModel.py').st_atime) #SPECIFIED
print(os.stat('osModel.py').st_size) #SPECIFIED

        #   TURN THE 'st_mtime' TO THE NORMAL FORMAT

time = os.stat('osModel.py').st_mtime
print(datetime.fromtimestamp(time))

        #   GET THE DETAILS OF A DIREC/SUB-DIREC & FILES WITH 'os.walk()' METHOD

for dirpath, dirnames, filenames in os.walk(paTH):
        print('Current path :', dirpath)
        print('Directories :', dirnames)
        print('Files :', filenames)





import os
print(dir(os))
variable = os.getcwd()
os.system("CMD COMMANDS")
os.chdir("new_path")
print(variable)
variable1 = os.listdir("C://Users//Windows10//OneDrive - OFPPT//Documents")
print(variable1)  
variable2 = os.path.join("C://Users//Windows10//OneDrive - OFPPT//Documents")
os.mkdir("lasaq")
print(variable2)
os.mkdir("Bilal123")
os.rmdir("Bilal123")
os.rename("Bilal123" , "Bilal")
print(os.stat("Bilal"))
print(os.stat("Bilal").st_size)
for dirpath , dirname , filename in os.walk(r"C:\Users\Windows10\Downloads"):
    print("The_path :" , dirpath)
    print("dir_name :" , dirname)
    print("file_name : " , filename)
    print()
path = "C:\\Users\\Windows10\\Downloads"
path0 = os.path.basename(path)
print(path0)
path0 = os.path.join(path)
print(path0)
# path0 = os.path.exists(path)
# print(path0)
path0 = os.path.split(path)
print(path0)
path0 = os.path.isfile(path)
print(path0)
path0 = os.path.isdir(path)
print(path0)
path0 = os.path.dirname(path)
print(path0)
path0 = os.path.normpath(path)
print(path0)
# ===========================================================================
import subprocess
P1 = subprocess.run("ls -l" , shell=True, capture_output=True, text=True)
print(P1.stdout)
P1 = subprocess.run("command" , shell=True , capture_outure=True , text=True)
print(P1.stdout)
# =============================================================================
import yaml
with open("example.yml", "w") as f:
    yaml.dump(data, f)
with open("example.yml" , "r")as f:
    data = yaml.safe_load(f)
    print(data)
# =================================================================================
import random
list = ["yahia","bilal","zakaria","mohamed"]
list = [True,False]
list = [1,2,3,4,5,6]
value = random.random()
value = random.uniform(5,9)
value = random.randint(3,9)
value = random.choice(list)
value = random.choices(list , k=3)
random.shuffle(my_list)
print(my_list)
print(value)
# ===================================================================================
import shutil
shutil.copy("source.txt", "destination.txt")
print("File copied.")
shutil.move("old_directory", "new_directory")
print("Directory moved.")
shutil.rmtree("directory_to_delete")
print("Directory deleted.")
shutil.make_archive("archive", "zip", "directory_to_archive")
print("Archive created.")
source_path = "C:\\Users\\Windows10\\OneDrive - OFPPT\\Documents\\Homework\\VR AND AR"
destination_path = "C:\\Users\\Windows10\\OneDrive - OFPPT\\Bureau\\Python exercices"
shutil.copy(source_path, destination_path)
# ======================================================================================