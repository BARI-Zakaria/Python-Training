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





