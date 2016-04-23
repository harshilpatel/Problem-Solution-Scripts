# BotClean Large- Hackerank  //initally for small modifies to large
# Author: harshil912@gmail.com
import math

# Head ends here
def next_move(posr, posc, dimy, dimx, board):
	x_closest_bot = 0
	y_closest_bot = 0
	for i in range(dimy):
		for j in range(dimx):
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


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)