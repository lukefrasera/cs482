import getopt, sys
sys.path.append("include/")
from sudoku import *

def main(argv):
	# PARSE ARGUMENTS
	try:
		opts, args = getopt.getopt(argv, "", [])
	except getopt.GetoptError as e:
		print "Argument Error: %s" % e
		sys.exit(2)

	# FILENAME
	filename = args.pop()
	try:
		file = open(filename)
	except IOError:
		print "Failed to open file: ",filename
		return
	puzzles = getBoards(file.read())
	
	puzzle_count = 0
	for puzzle in puzzles:
		print "Puzzle #",puzzle_count,": ",puzzle
		puzzle_count+=1
	print "\n"

	# SOLVE EACH PUZZLE IN FILE
	solution = 0
	puzzle_count = 0
	for puzzle in puzzles:
		#solution.append(solve(puzzle))
		print "Solution #",puzzle_count,": ",solve(puzzle),"\n"
		puzzle_count += 1

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
