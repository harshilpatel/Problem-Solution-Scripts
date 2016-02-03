a = input().split()
b = a[1]
a = a[0]

items = [int(x) for x in input().split()]
ways = 0
solutions = []
def possible_ways(list):
	ways = 0
	temp_list = []
	temp_count = 0
	for i in range(len(list)):
		temp_count +=list[i]
		possible_ways(list[])


	return ways


print(str(possible_ways([2,3,4])))
