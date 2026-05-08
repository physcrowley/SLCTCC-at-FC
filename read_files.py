"""Gabarit pour l'accès à un fichier
"""

INPUT_PATH = "SLC_2024/Input/DATA11.txt" 

data = []
with open(INPUT_PATH, 'r') as file:
    data = file.readlines()

end = -1
for pos in range(len(data)):
   if pos == end + 1:
     steps = int(line)
     end = pos + steps
     continue
   for _ in range(num):
print(data)

