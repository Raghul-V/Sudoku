import check_sudoku as check


def solve_sudoku(grid, place_holder=0):
	""" Solves a sudoku grid and returns it if possible 
	else returns 'No Solution'... """
	for i in range(9):
		for j in range(9):
			if grid[i][j] == place_holder:
				# Checks all numbers from 1 to 9. if a number is 
				# possible then places the number. Tries to solve 
				# the grid recusively until finds the right number
				for guess in range(1, 10):
					if check.is_position_possible(grid, i, j, guess):
						grid[i][j] = guess
						solve_sudoku(grid, place_holder)
						if check.is_sudoku_correct_2(grid):
							return grid
					# Backtracks the positions which were 
					# replaced if the previous recursion 
					# cannot solve the grid
					grid[i][j] = place_holder
				# If the current element is a place_holder 
				# but has no possiblities for all 1 to 9
				# then returns 'No Solution'
				return "No Solution"

	# Returns the solved grid if possible to solve 
	# else returns 'No Solution'
	if check.is_sudoku_correct_2(grid):
		return grid
	return "No Solution"


if __name__ == "__main__":
	test_grid = [[0, 2, 3, 4, 5, 0, 7, 8, 9],
				 [0, 5, 0, 7, 8, 9, 0, 2, 3],
				 [0, 8, 0, 0, 2, 3, 0, 5, 0],
				 [0, 3, 0, 5, 0, 0, 8, 0, 0],
				 [0, 0, 0, 8, 0, 0, 0, 3, 0],
				 [0, 0, 1, 0, 3, 0, 0, 0, 0],
				 [0, 4, 0, 0, 0, 0, 0, 1, 0],
				 [0, 7, 0, 0, 1, 0, 0, 4, 0],
				 [0, 1, 2, 0, 4, 0, 0, 7, 0]]

	print(solve_sudoku(test_grid, 0))



