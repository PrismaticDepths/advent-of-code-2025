"""https://adventofcode.com/2025/day/2"""

def read_puzzle_input(text:str):
	return text.split(",")

with open("input.txt","r") as input_file:
	ids:str = read_puzzle_input(input_file.read())

print(f"Answer: {None}")