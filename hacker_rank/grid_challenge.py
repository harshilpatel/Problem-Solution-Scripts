# https://www.hackerrank.com/challenges/grid-challenge
# harshil912@gmail.com
# !py3


test_case = int(input())

def arrange(grid,dic):
	grid2 = []
	for i in range(len(grid)):
		grid[i].sort()

	for i in range(len(grid)):
		for j in range(1,len(grid)):
			if grid[i][j] < grid[i][j-1]:
				return 'NO'
	for i in range(1,len(grid)):
		for j in range(len(grid)):
			if grid[j][i] < grid[j][i-1]:
				return 'NO'
	return "YES"

	pass


def main():
	a = list('abcdefghijklmnopqrstuvwxyz')
	dic = {}
	for i in range(len(a)):
		dic[i] = a[i]
	lines = int(input())
	grid = []
	for i in range(lines):
		temp = list(input().strip())
		grid.append(temp)
	solve = False
	print(arrange(grid,dic))

for i in range(test_case):
	main()