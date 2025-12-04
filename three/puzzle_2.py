"""https://adventofcode.com/2025/day/3#part2"""

def read_puzzle_input(text:str):
	return text.splitlines()

with open("input.txt","r") as input_file:
	voltages:str = read_puzzle_input(input_file.read())

current:int = 0
times = 12
for i in voltages:
	highest_numbers:int = [0 for n in range(times)]
	index:int = -1
	cur = -1
	for n in range(times-1):
		cur:int = index
		for j in i[index+1:]:
			cur += 1
			if int(j) > highest_numbers[n] and cur < len(i)-(times-(n+1)):
				highest_numbers[n] = int(j)
				index = cur
	for j in i[index+1:]:
		if max(int(j), highest_numbers[times-1]) == int(j):
			highest_numbers[times-1] = int(j)
	current += int("".join(map(lambda f: str(f),highest_numbers)))

print(f"Answer: {current}")