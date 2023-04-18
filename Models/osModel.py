import os

        #   TO GET YOUR LOCAL LOCATION
print(os.getcwd())

        #    TO CHANGE YOUR LOCATION
patH = "C:\\Users\\Zakaria\\Desktop\\Python"
os.chdir(patH)

        #   TO LIST THE CONTENT INSIDE A DIRECTORY
print(os.listdir())

        #   TO MAKE/CREATE A DIRECTORY OR MAKE/CREATE A DIRECTORY WITH SUB-DIRECTORY
os.mkdir('Models')
os.makedirs('Models1/OSModel/MMM')

        #   TO REMOVE A DIRECTORY OR REMOVE A DIRECTORY WITH SUB-DIRECTORY

os.rmdir('Models1/OSModel/MMM')
os.removedirs('Models1/OSModel')

