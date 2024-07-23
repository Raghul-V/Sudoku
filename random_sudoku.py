from solve_sudoku import solve_sudoku
from random import randrange


def random_sudoku(level=0, place_holder=0):
	""" Creates a random solvable sudoku board and 
	returns the unsolved sudoku board and its solution... """
	grid = [[0 for _ in range(9)] for _ in range(9)]
	# Fills some random places with numbers 1 to 9
	# so that it will not always return a same board
	for i in range(1, 10):
		row = randrange(9)
		col = randrange(9)
		grid[row][col] = i
	# Solves the board with was filled with numbers from 1 to 9
	# so that it is confirm that the board is solvable
	solution = [lst.copy() for lst in solve_sudoku(grid, 0)]
	# maps the number of obstacles that should be placed 
	# in the board based on the level
	difficulty = {
		0: 10,
		1: 15,
		2: 25,
		3: 35,
		4: 50,
		5: 65,
		6: 75,
		7: 90,
		8: 100
	}
	# finds the number of obstacles for the given level board
	min_level, max_level = min(difficulty), max(difficulty)
	if level in difficulty:
		x = difficulty[level]
	elif type(level) == int:
		if level < min_level:
			x = difficulty[min_level]
		elif level > max_level:
			x = difficulty[max_level]
	else:
		return "Wrong Input..."
	# places those obstacles on some random positions
	for i in range(x):
		row = randrange(9)
		col = randrange(9)
		grid[row][col] = place_holder
	# returns the unsolved board and its solution...
	return grid, solution

