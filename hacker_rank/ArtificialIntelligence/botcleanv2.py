# BotClean Blind- Hackerank  
# Author: harshil912@gmail.com
# https://www.hackerrank.com/challenges/botcleanv2

import math
# Head ends here
def next_move(posr, posc, board):
	x_closest_bot = 0
	y_closest_bot = 0
	for i in range(5):
		for j in range(5):
			if board[i][j] == 'd':
				if posr == i and posc == j:
					print("CLEAN")
					return
				x = j
				y = i
				if posr < y:
					print("DOWN")	
					return	
				elif posr > y:
					print("UP")
					return
				if posc < x:
					print("RIGHT")
					return
				elif posc > x:
					print("LEFT")
					return
	for i in [4,3,2,1,0]:
		for j in [4,3,2,1,0]:
			if board[i][j] == 'o':
				x = j
				y = i
				if posr < y:
					print("DOWN")	
					return	
				elif posr > y:
					print("UP")
					return
				if posc < x:
					print("RIGHT")
					return
				elif posc > x:
					print("LEFT")
					return




# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)