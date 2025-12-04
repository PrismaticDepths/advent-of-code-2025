"""https://adventofcode.com/2025/day/1#part2"""

def rotate_lock(current:int,offset:int):

	cur = current
	buf = offset
	sign = 1 if abs(offset)==offset else -1
	count = 0
	while buf != 0:
		cur += sign
		cur %= 100
		if cur == 0: count+=1
		buf -= sign

	return (current+offset)%100, count


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
	lock,zer = rotate_lock(lock,i)
	counter += zer

print(f"Answer: {counter}")