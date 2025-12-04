"""https://adventofcode.com/2025/day/2#part2"""

def read_puzzle_input(text:str):
	return list(map(lambda f: f.split("-"),text.split(",")))

with open("input.txt","r") as input_file:
	ids:str = read_puzzle_input(input_file.read())

total = 0
for sequence in ids:
	for i in range(int(sequence[0]),int(sequence[1])+1):
		# find pattern
		istring = str(i)
		buffer = ""
		bpointer = 0
		# istring = "12341234"
		# shift to istring[0] -> 1, does not match anything in buffer (buffer="") so add index to buffer
		# shift to istring[1] -> 2, does not match anything in buffer (buffer="1") so add index to buffer
		# shift to istring[2] -> 3, does not match anything in buffer (buffer="12") so add index to buffer
		# shift to istring[3] -> 4, does not match anything in buffer (buffer="123") so add index to buffer
		# shift to istring[4] -> 1, matches start of buffer (1), remove istring[4], shift to buffer[1]
		# shift to istring[5] -> 2, matches position in buffer (2), remove istring[5]
		#...
		# repeat until at the end of the string, if buffer empty then there is a pattern
		# fails if there's an odd number of patterns ("123412341234")
		for pointer in range(len(istring)-1):
			try:
				if istring[pointer] == buffer[bpointer]:
					bpointer+=1
					print("n")
				else:
					buffer += istring[pointer]
					bpointer = 0
					print('y')
			except IndexError:
					buffer += istring[pointer]
					bpointer = 0
		print(buffer)


print(f"Answer: {total}")