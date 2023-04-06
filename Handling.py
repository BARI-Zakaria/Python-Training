f = open("demofile.txt", "w")
f.write("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad, magnam.")
f.close()

f = open("demofile1.txt", "x")
f.write("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad, magnam.")
f.close()

f = open("demofile5.txt", "a")
f.write("Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ad, magnam.")
f.close()

f = open("demofile15.txt", "r")
print(f.read())