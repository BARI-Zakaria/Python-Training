import os
from datetime import datetime
import subprocess
# print(os.stat('Training\\Exercices.py').st_size)
# print(os.stat('Training\\Exercices.py').st_atime)

# time = os.stat('Training\\Exercices.py').st_mtime
# print(datetime.fromtimestamp(time))
# Path = r"C:\Users\Zakaria\Desktop\Python-Training\Models"
# for dirpath, dirnames, filenames in os.walk(Path):
#         print('Current path :', dirpath)
#         print('Directories :', dirnames)
#         print('Files :', filenames)

import shutil
Archive = shutil.make_archive("archive", "zip", r"C:\Users\Zakaria\Desktop\Python-Training\HandlingFiles")
print(Archive)
# shutil.move("old_directory", "new_directory")
# print("Directory moved.")
# shutil.rmtree("directory_to_delete")
# print("Directory deleted.")
# shutil.make_archive("archive", "zip", "directory_to_archive")
# print("Archive created.")
# source_path = "C:\\Users\\Windows10\\OneDrive - OFPPT\\Documents\\Homework\\VR AND AR"
# destination_path = "C:\\Users\\Windows10\\OneDrive - OFPPT\\Bureau\\Python exercices"
# shutil.copy(source_path, destination_path)