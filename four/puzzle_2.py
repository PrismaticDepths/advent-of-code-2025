"""https://adventofcode.com/2025/day/4"""
import copy,time

def read_puzzle_input(text:str):
	t = text.splitlines()
	return list(map(lambda f: list(f), t))

with open("input.txt","r") as input_file:
	grid:list[list[str]] = read_puzzle_input(input_file.read())

goriginal = copy.deepcopy(grid)
gcopy = copy.deepcopy(grid)
accessible_sheets = 1
total = 0
while accessible_sheets > 0:
	buf = 0
	grid = copy.deepcopy(gcopy)
	for y in range(0,len(grid)):
		for x in range(len(grid[y])):
			assert grid[y][x] in ['@','.']
			if grid[y][x] == '.': continue
			elif grid[y][x] == '@':
					a = []
					if y-1 >= 0: a.extend([
						grid[y-1][x-1] if x-1 >= 0 else ".",
						grid[y-1][x],
						grid[y-1][x+1] if x+1 <= len(grid[y-1])-1 else "."
						])
					a.extend([
						grid[y][x-1] if x-1 >= 0 else ".",
						grid[y][x+1] if x+1 <= len(grid[y])-1 else "."
						])
					if y+1 <= len(grid)-1: a.extend([
						grid[y+1][x-1] if x-1 >= 0 else ".",
						grid[y+1][x],
						grid[y+1][x+1] if x+1 <= len(grid[y+1])-1 else "."
						])
					c = 0
					for i in a: 
						if i == '@': c+=1
					if c < 4: 
						buf+=1
						gcopy[y][x] = '.'
	accessible_sheets=buf
	total += buf

print(f"Answer: {total}")
#print("\n".join(list(map(lambda f: "".join(f),gcopy))))