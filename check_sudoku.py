import numpy as np


def is_position_possible(grid, row, col, elem):
	""" Checks an element can be placed in a certain position or not... """
	np_grid = np.array(grid)
	# Replaces the given position with a dummy element
	# So that it should not appear again in the corresponding 
	# row, column, or box
	np_grid[row, col] = 0

	# Checks the given element is a number within 1 to 9
	# Then checks it doesn't repeats anywhere in the 
	# corresponding row, column, or box
	if elem in range(1, 10):
		if elem not in np_grid[row]:
			if elem not in np_grid[:, col]:
				# b_row -> box starting row
				# b_col -> box starting column
				b_row, b_col = row//3*3, col//3*3
				if elem not in np_grid[b_row:b_row+3, b_col:b_col+3]:
					return True

	return False

# Best for space complexity...
def is_sudoku_correct_1(grid):
	""" Checks a sudoku grid is correctly completed or not... """
	np_grid = np.array(grid)

	# Checks the sum of each rows, columns, and boxes equals to 45.
	# because sum(range(1, 10)) = 45. if not equal returns false
	try:
		for i in range(9):
			if sum(np_grid[i]) != 45:
				return False
			if sum(np_grid[:, i]) != 45:
				return False
		for i in range(3):
			for j in range(3):
				if sum(sum(np_grid[i*3:i*3+3, j*3:j*3+3])) != 45:
					return False
	# If there is any non integer in the grid, then returns false
	except:
		return False

	return True

# Best for time complexity...
def is_sudoku_correct_2(grid):
	""" Check a sudoku grid is correctly completed or not. 
	This is approximately twice as fast as is_grid_correct_1 
	but has a little bit more space complexity... """
	if len(grid) != 9:
		return False

	col, box = [{} for j in range(9)], [{} for j in range(9)]

	# Store every element of the grid in three dictionaries 
	# namely row, column, and box.
	for i in range(9):
		if len(grid[i]) != 9:
			return False
		# Stores the elements if it's within the range [1, 9] 
		# and if it not is already there, else returns false
		row = {}
		for j in range(9):
			present = grid[i][j]
			if present in range(1, 10):
				if present in row:
					return False
				if present in col[j]:
					return False
				if present in box[i//3*3 + j//3]:
					return False

				row[present] = True
				col[j][present] = True
				box[i//3*3 + j//3][present] = True
			else:
				return False
	# returns true if no element in each dictionaries repeats
	return True

