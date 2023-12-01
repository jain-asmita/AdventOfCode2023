with open("Inputs/Day1.txt", "r") as input:
    input = input.read()
 
input_list = input.split("\n")
 
mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}
 
def findDigit(line, mapping, last=False, check_words=False):
    if last:
        startIndex = len(line) - 1
        endIndex = -1
        increment = -1
    else:
        startIndex = 0
        endIndex = len(line)
        increment = 1
    for index in range(startIndex,endIndex,increment):
        letter = line[index]
        if letter.isdigit():
            return int(letter)
        if check_words:
            for word, number in mapping.items():
                if line[index:].startswith(word):
                    return number
     
answer_part_1 = 0
for line in input_list:
    answer_part_1 += findDigit(line, mapping, last=False, check_words=False) * 10
    answer_part_1 += findDigit(line, mapping, last=True, check_words=False)
print(answer_part_1)
 
answer_part_2 = 0
for line in input_list:
    answer_part_2 += findDigit(line, mapping, last=False, check_words=True) * 10
    answer_part_2 += findDigit(line, mapping, last=True, check_words=True)
print(answer_part_2)