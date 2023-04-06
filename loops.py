# i+= 1 <=> i = i+1
# THE WHILE LOOP 
i = 1
while i < 6:
  print(i)
  i += 1

i = 6
while i < 99:
  print(i)
  i += 1

  
i = 1
while i < 99:
  print(i)
  i += 1
  
  if i == 15:
    break

# THE FOR LOOP

tent = [1, 2, 3, 4, 5, 6, 7, 8]
for x in tent:
    print(x)

    if x == 10:
        break
    else:
        continue

Ramadan = ["Rghayef", "Briwate", "Chebakia", "Harira", "Btboute", "Houte"]
for x in Ramadan:
    print(x)
    if x == "Harira":
        continue