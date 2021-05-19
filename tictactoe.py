import random
import time


# initial empty board
board = {
	1: " ", 2: " ", 3: " ",
	4: " ", 5: " ", 6: " ",
	7: " ", 8: " ", 9: " ",
}

taken_pos = 0


def print_board():
	"""prints the board with rows and columns"""
	print()
	for i in range(1, 10):
		if i == 3 or i == 6:
			print(board[i])
			print("- - -")
		elif i == 9:
			print(board[i])
		else:
			print(board[i], end="|")
	print()


def ai_choice():
	"""randomly picks a position that is not already taken"""
	while True:
		choice = random.randint(1, 9)
		if board[choice] == " ":
			return choice


def usr_choice():
	"""gets valid position (1-9) from user that is not already taken"""
	while True:
		try:
			choice = int(input("Enter position: "))
			if not 1 <= choice <= 9:
				print("Please enter a valid position")
				continue
			elif board[choice] != " ":
				print("That position is taken")
				continue
			return choice

		except ValueError:
			print("Please enter a number")


def mark(pos, shape):
	"""marks user's or computer's choice on the board"""
	global taken_pos
	board[pos] = shape
	taken_pos += 1


def win_check():
	"""checks for matching rows, columns or diagonal lines"""
	# matching rows
	if board[1] == board[2] == board[3] and board[1] != " ":
		return True
	elif board[4] == board[5] == board[6] and board[4] != " ":
		return True
	elif board[7] == board[8] == board[9] and board[7] != " ":
		return True

	# matching columns
	elif board[1] == board[4] == board[7] and board[1] != " ":
		return True
	elif board[2] == board[5] == board[8] and board[2] != " ":
		return True
	elif board[3] == board[6] == board[9] and board[3] != " ":
		return True

	# matching diagonals
	elif board[1] == board[5] == board[9] and board[1] != " ":
		return True
	elif board[3] == board[5] == board[7] and board[3] != " ":
		return True


if __name__ == "__main__":

	"""gets user shape choice"""
	while True:
		usr_shape = input("What shape would you like to be? (X or O): ")
		if usr_shape.upper() == "X":
			ai_shape = "O"
		elif usr_shape.upper() == "O":
			ai_shape = "X"
		else:
			print("Invalid shape")
			continue
		break

	print(f"You: {usr_shape}")
	print(f"Computer: {ai_shape}")

	while True:
		if taken_pos != 9:
			time.sleep(1)
			mark(ai_choice(), ai_shape)
			print_board()
			if win_check():
				print("Computer wins!")
				break

		if taken_pos != 9:
			mark(usr_choice(), usr_shape)
			print_board()
			if win_check():
				print("You win!")
				break
			continue

		print("Tie!")
		break

	print("Game finished!")
