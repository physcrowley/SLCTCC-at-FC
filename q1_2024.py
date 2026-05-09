"""Solution à SLC 2024 Q1 avec DATA11.txt"""

INPUT_PATH = "SLC_2024/Input/DATA11.txt"

# PLACER LES DONNÉES DU FICHIER EN MÉMOIRE
data = []
with open(INPUT_PATH, "r") as file:
    data = file.readlines()

# TRAITER LES DONNÉES

## Créer une liste pour les calculs utilisant des tranches de liste
calculations = []
pos = 0
while pos < len(data):
    size = int(data[pos])
    first = pos + 1
    next_pos = first + size
    if next_pos == len(data):
        calculations.append(data[first:])
    else:
        calculations.append(data[first:next_pos])
    pos = next_pos

## Calculer les résultats
for calc in calculations:
    result = 0
    for op_code in calc:
        op_parts = op_code.split()
        match(op_parts[0]):
            case "MUL": 
                result *= int(op_parts[1])
            case "INC": 
                result += 1
            case "DEC": 
                result -= 1
    print(result)