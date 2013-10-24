import getopt, sys

def main(argv):
	# PARSE ARGUMENTS
	try:
		opts, args = getopt.getopt(argv, "", [])
	except getopt.GetoptError as e:
		print "Argument Error: %s" % e
		sys.exit(2)

	# FILENAME
	filename = args.pop()
	file = open(filename)
	puzzles = getBoards(file.read())

	print puzzles

	# SOLVE EACH PUZZLE IN FILE
	# for puzzle in puzzles:
	# 	solution.append(sudokuSolve(puzzle))

def getBoards(string):
	puzzles=[]
	digits='123456789'
	board = ''
	for c in string:
		if c in digits or c in '0.':
			board += c
		if len(board)==81:
			puzzles.append(board)
			board=''
	return puzzles


if __name__ == '__main__':
	main(sys.argv)