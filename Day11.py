with open("Inputs/Day11.txt", "r") as input:
    input = input.read()

input_list = input.split("\n")

input_grid = []
for line in input_list:
    input_grid.append([*line])

nRows = len(input_list)
nCols = len(input_list[0])

empty_rows = []
empty_cols = []

for rowNum in range(0, nRows):
    if "#" not in input_grid[rowNum]:
        empty_rows.append(rowNum)

for colNum in range(0, nCols):
    if "#" not in [i[colNum] for i in input_grid]:
        empty_cols.append(colNum)

def generateGalaxyCoords(expansion_factor):
    galaxies = set()
    row = 0
    col = 0
    actual_row = 0
    actual_col = 0

    for line in input_list:
        if row in empty_rows:
            actual_row += (expansion_factor - 1)
        for letter in line:
            if col in empty_cols:
                actual_col += (expansion_factor - 1)
            if letter == "#":
                galaxies.add(tuple([actual_row, actual_col]))
            col += 1
            actual_col += 1
        col = 0
        actual_col = 0
        row += 1
        actual_row += 1
    return galaxies

part1_answer = 0
galaxies = generateGalaxyCoords(2)
for gal1 in galaxies:
    for gal2 in galaxies:
        part1_answer += (abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]))
print(part1_answer / 2)

part2_answer = 0
galaxies = generateGalaxyCoords(1000000)
for gal1 in galaxies:
    for gal2 in galaxies:
        part2_answer += (abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]))
print(part2_answer / 2)

