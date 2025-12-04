"""https://adventofcode.com/2025/day/2#part2"""

def read_puzzle_input(text:str):
	return list(map(lambda f: f.split("-"),text.split(",")))

with open("input.txt","r") as input_file:
	ids:str = read_puzzle_input(input_file.read())

total = 0
for sequence in ids:
	for i in range(int(sequence[0]),int(sequence[1])+1):
		if len(str(i))%2 == 1: continue
		halves = []
		halves.append(str(i)[:len(str(i))//2])
		halves.append(str(i)[len(str(i))//2:])
		if halves[0] == halves[1]: 
			total += int(halves[0]+halves[1])

print(f"Answer: {total}")