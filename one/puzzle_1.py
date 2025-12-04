"""https://adventofcode.com/2025/day/1"""
import math

def rotate_lock(current:int,offset:int):

	return (current+offset) % 100

def read_puzzle_input(text:str):
	rotations:list[int] = []
	for i in text.splitlines():
		assert i[0].upper() in ["L","R"]
		if i[0].upper() == "L": # ROTATE TOWARDS LOWER NUMS
			rotations.append(-1*int(i[1:]))
		elif i[0].upper() == "R": # ROTATE TOWARDS HIGHER NUMS
			rotations.append(int(i[1:]))
	return rotations

with open("input.txt","r") as input_file:
	rotations = read_puzzle_input(input_file.read())

lock:int = 50
counter:int = 0
for i in rotations:
	lock = rotate_lock(lock,i)
	if lock == 0: counter += 1

print(f"Answer: {counter}")