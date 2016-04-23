#!/bin/python
# Author: harshil912@gmail.com
# Click - o - mania
# https://www.hackerrank.com/challenges/click-o-mania


def check_if_neightbour(i,j,grid,x,y):
	temp_connected_regions = []
	color = grid[i][j]
	if i<x and j<y:
		pass
	else:
		return False
	try:
		for a in [-1,0,1]:
			for b in [-1,0,1]:
				try:
					if grid[a+i][b+j] == grid[i][j] and 0<=a+i<x and 0<=b+j<y:
						print(str(a+i) + str(b+j))
						temp_connected_regions.append(str(a+i) + str(b+j))
						neighbours = check_if_neightbour(a+i,b+j,grid,x,y)
						if neighbours != False:
							for i in neighbours:
								temp_connected_regions.append(i)
				except:
					pass
		if len(temp_connected_regions) == 0:
			return False
		else:
			return list(set(temp_connected_regions))
	except:
		return False
		pass

def nextMove(x, y, color, grid):
	x_connected = 0
	y_connected = 0
	color_count = {}
	connected_regions = []
	colors = []
	for i in range(x):
		for j in range(y):
			if grid[i][j] not in colors:
				colors.append(grid[i][j])
			if len(colors) == color:
				break
	for i in reversed(range(x)):
		for j in reversed(range(y)):
			if grid[i][j] != "-":
				result = check_if_neightbour(i,j,grid,x,y)
				if result != False:	connected_regions.append(result)


	max_connected_region = max([len(i) for i in connected_regions])
	for i in connected_regions:
		if len(i) == max_connected_region:
			print(i[0][0] +" "+ i[0][1])
			return

	# for i in range(color):
	# 	for j in range(x):
	# 		for k in range(y):
	# 			if grid[j][k] != '-':
	# 				try:
	# 					get_color = color_count[grid[j][k]]
	# 					color_count[grid[j][k]] += 1
	# 				except:
	# 					color_count[grid[j][k]] = 1
	# max_color = max(list(color_count.values()))
	# max_color_name = ''
	# for i,j in color_count.items():
	# 	if max_color == j:
	# 		max_color_name = i
	# for i in list(reversed(range(x))):
	# 	for j in range(y):
	# 		if grid[i][j] == max_color_name:
	# 			print(str(i) +" "+ str(j))
	# 			return

if __name__ == '__main__':
    x,y,k = [ int(i) for i in input().strip().split() ] 
    grid = [[i for i in str(input().strip())] for _ in range(x)] 
    nextMove(x, y, k, grid)
