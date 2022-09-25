# Section 6 – Modular Programming
# Example 55 – A Procedure with Multiple Parameters

def displayWinner(player1,player2):
	player1Wins = 0
	player2Wins = 0
	draws = 0
	for loop in range(len(player1)):
		if player1[loop]>player2[loop]:
			player1Wins = player1Wins + 1
		if player2[loop]>player1[loop]:
			player2Wins = player2Wins + 1
		if player2[loop]==player1[loop]:
			draws = draws + 1
	print("Player 1 has",player1Wins,"wins.")
	print("Player 2 has",player2Wins,"wins.")
	print("There were",draws,"draws.")

# Main Program
player1 = [4,6,8,5,6]
player2 = [2,9,8,5,3]
displayWinner(player1,player2)


