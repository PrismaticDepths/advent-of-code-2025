"""https://adventofcode.com/2025/day/3"""

def read_puzzle_input(text:str):
	return text.splitlines()

with open("input.txt","r") as input_file:
	voltages:str = read_puzzle_input(input_file.read())

current:int = 0
for i in voltages:
	highest_first_number:int = 0
	highest_second_number:int = 0
	first_index:int = 0
	cur:int = -1
	for j in i:
		cur += 1
		if int(j) > highest_first_number and cur < len(i)-1:
			highest_first_number = int(j)
			first_index = cur
	for j in i[first_index+1:]:
			highest_second_number = max(int(j),highest_second_number)
	current += int(str(highest_first_number)+str(highest_second_number))
print(f"Answer: {current}")