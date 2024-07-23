from solve_sudoku import solve_sudoku
from random_sudoku import random_sudoku
import time, os
import numpy as np

# change to increase the difficulty of the game
START_LEVEL = 100


def print_board(board, show_place_holders=True):
	print()
	for row in board:
		if show_place_holders:
			print(" "*15, *[(i if type(i) == int else " ") for i in row],
				sep="   ", end="\n\n")
		else:
			print(" "*15, *[(i if i in range(1, 10) else "_") for i in row],
				sep="   ", end="\n\n")
	print()
	return board


def get_inputs(grid, place_holder=0):
	while True:
		try:
			row = int(input(" Enter a row (1 to 9): "))
			if row not in range(1, 10):
				print(" That's not even in the board...")
				time.sleep(1)
				continue
			break
		except:
			print(" Enter a valid row...")
			time.sleep(1)
	while True:
		try:
			col = int(input(" Enter a column (1 to 9): "))
			if col not in range(1, 10):
				print(" That's not even in the board...")
				time.sleep(1)
				continue
			break
		except:
			print(" Enter a valid column...")
			time.sleep(1)
	if grid[row-1][col-1] in range(1, 10):
		return get_inputs(grid, place_holder=place_holder)
	while True:
		try:
			elem = int(input(" Enter a number to place (1 to 9): "))
			if elem not in range(1, 10):
				print(" That's not a valid number to fit this board...")
				time.sleep(1)
				continue
			break
		except:
			print(" Enter a valid number...")
			time.sleep(1)

	return row, col, elem


def play_sudoku(level=0):
	caption_logo = r"""
                                         ________   ________   ________ 
                                        |__|__|__| |__|__|__| |__|__|__|
                                        |__|__|__| |__|__|__| |__|__|__|
                                        |__|__|__| |__|__|__| |__|__|__|
  ___  _  _ ___   __  _  _ _  _          ________   ________   ________ 
 |___  |  | |  \ |  | |_/  |  |         |__|__|__| |__|__|__| |__|__|__|
  ___| |__| |__/ |__| | \_ |__|         |__|__|__| |__|__|__| |__|__|__|
                                        |__|__|__| |__|__|__| |__|__|__|
                                         ________   ________   ________ 
                                        |__|__|__| |__|__|__| |__|__|__|
                                        |__|__|__| |__|__|__| |__|__|__|
                                        |__|__|__| |__|__|__| |__|__|__|

 =======================================================================
"""
	game_over = False
	total_life = 25
	life = total_life
	life_logo = "["+ "-"*(total_life-life) + "/"*life +"]"

	board, solution = random_sudoku(level)

	os.system("cls") # for windows
	# os.system("clear") # for linux, or mac os
	print(caption_logo)
	print(" "*(70-total_life) + life_logo)
	print()
	print_board(board, show_place_holders=False)

	while not game_over:
		row, col, elem = get_inputs(board)
		if board[row-1][col-1] != 0:
			print(" That place is already filled...")
			time.sleep(2)
		elif solution[row-1][col-1] == elem:
			board[row-1][col-1] = elem
			print(" Correct !!!...")
			time.sleep(2)
		else:
			print(" Wrong number. It cannot be placed there...")
			time.sleep(2)
			life -= 5

		life_logo = "["+ "-"*(total_life-life) + "/"*life +"]"

		if life <= 0 or 0 not in np.array(board):
			game_over = True
			board = solution

		os.system("cls") # for windows
		# os.system("clear") # for linux, or mac os
		print(caption_logo)
		print(" "*(70-total_life) + life_logo)
		print()
		print_board(board, show_place_holders=False)

		if life <= 0:
			print("\n You Lose !!!...\n")
			time.sleep(1)
		elif 0 not in np.array(board):
			print("\n You Won !!!...\n")
			time.sleep(1)

		while game_over:
			play_again = input(" Want to play again (y/n)? ").lower()
			if play_again == "yes" or play_again == "y":
				if life > 0:
					level += 1
				play_sudoku(level)
				return True
			elif play_again == "no" or play_again == "n":
				break
			else:
				print(" Please enter y (or) n ...")

	return True


if __name__ == "__main__":
	play_sudoku(level=START_LEVEL)
