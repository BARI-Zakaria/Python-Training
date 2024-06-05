# # "w" - Write - Opens a file for writing, creates the file if it does not exist
# f = open("demofile.yaml", "a")
# f.write("REGIONAL PYTHON.")
# f.close()
import yaml
Text = "TANGIER"
with open("Text.yaml", "a") as f:
    append = yaml.dump(Text, f)
    print(append)

with open("Text.yaml", "r") as f:
    read = yaml.safe_load(f)
    print(read)

# # "x" - Create - Creates the specified file, returns an error if the file exists
# f = open("demofile1.txt", "x")
# f.write("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad, magnam.")
# f.close()

# # "a" - Append - Opens a file for appending, creates the file if it does not exist
# f = open("demofile5.txt", "a")
# f.write("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad, magnam.")
# f.close()

# # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# f = open("demofile15.txt", "r")
# print(f.read())