class TicTacToe:

	def __init__(self):
		self.main_board = [str(i) for i in range(1, 10)]
		self.turn = 'x'

	def print_board(self):
		print(f"| {self.main_board[0]} | {self.main_board[1]} | {self.main_board[2]} |")
		print("-------------------------")
		print(f"| {self.main_board[3]} | {self.main_board[4]} | {self.main_board[5]} |")
		print("-------------------------")
		print(f"| {self.main_board[6]} | {self.main_board[7]} | {self.main_board[8,]} |")

	def check_winner(self):
		winning_combinations = [
			[0, 1, 2],
			[3, 4, 5],
			[6, 7, 8],
			[0, 3, 6],
			[1, 4, 7],
			[2, 5, 8],
			[0, 4, 8],
			[2, 4, 6]
		]

		for combo in winning_combinations:
			if self.main_board[combo[0]] == self .main_board[combo[1]] == self.main_board[combo[2]]:
				if slef.main_board[combo[0]] == 'x':
					return 'x'
				elif sel.main_board[combo[0]] == 'o':
					return 'o'

		if all(cell in ['x', 'o'] for cell in self.main_board):
			return 'draw'
	
		return None


	def play_game(self):
		print("Welcome to Tic Tac Toe!")
		self.print_board()
		print("Player 'x' goes first. Enter a number to place 'x' in:  ")

		while True:
			try: 
				num_input = int(input())
				if num_input < 1 or num_input > 9:
					print("Invalid input; re-enter slot number:  ")
					continue
			except ValueError:
				print("Invalid input; re-enter slot number:   ")
				continue

			if self.main_board[num_input - 1] not in ['x', 'o']:
				self.main_board[num_input - 1] = self.turn
				self.print_board()
				winner = self.check_winner()
	
				if winner:
					if winner == 'draw':
						print("It is a draw! Thanks for playing.")
					else:
						print(f"Congratulations! {winner} has won! Thanks for playing.")
					break

		
				self.turn = 'o' if self.turn == 'x' else 'x'
			else:
				print("slot already take, re-enter slot number:  ")

if __name__ == "__main__":
	game = TicTacToe()
	game.play_game()
	