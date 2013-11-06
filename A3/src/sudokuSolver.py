import getopt, sys, os
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
	
	# DISPLAY PUZZLES
	for i, puzzle in enumerate(puzzles):
		print "Puzzle #",i,": ",puzzle
	print "\n"

	# SOLVE EACH PUZZLE IN FILE
	for i, puzzle in enumerate(puzzles):
		solution = solve(puzzle)
		print "Solution #",i,": Solved:", solved(solution)
		if solved(solution):
			display(solution)

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
