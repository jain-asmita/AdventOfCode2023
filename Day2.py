with open("Inputs/Day2.txt", "r") as input:
    input = input.read()

input_list = input.split("\n")

games = []
for line in input_list:
    line = line.split(": ")[1]
    line_list = []
    for component in line.split("; "):
        stop = False
        dict = {}
        if " red" in component:
            red_part = int(component.split(" red")[0][-2:].strip())
            dict.update({"red": red_part})
        if " blue" in component:
            blue_part = int(component.split(" blue")[0][-2:].strip())
            dict.update({"blue": blue_part})
        if " green" in component:
            green_part = int(component.split(" green")[0][-2:].strip())
            dict.update({"green": green_part})
        line_list.append(dict)
    games.append(line_list)

p1_answer = 0
game_num = 0
for game in games:
    game_num += 1
    game_valid = True
    for round in game:
        if round.get("red", 0) > 12 or round.get("green", 0) > 13 or round.get("blue", 0) > 14:
            game_valid = False
    if game_valid:
        p1_answer += game_num

print(p1_answer)

p2_answer = 0
for game in games:
    min_blue = 0
    min_red = 0
    min_green = 0
    for round in game:
        reds = round.get("red", 0)
        if reds > min_red:
            min_red = reds
        greens = round.get("green", 0)
        if greens > min_green:
            min_green = greens
        blues = round.get("blue", 0)
        if blues > min_blue:
            min_blue = blues
    p2_answer += (min_blue * min_green * min_red)

print(p2_answer)