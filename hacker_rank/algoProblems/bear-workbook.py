# harshil912@gmail.com
# https://www.hackerrank.com/challenges/bear-and-workbook
# Accepted
import math
n,k = input().split()
n = int(n);k = int(k)

problems =[int(x) for x in input().split()]
book = []
# problem_set = {}
page = 1
result = 0
for i in problems:
	required_pages = math.ceil(i/k)
	problem_start = 1
	for j in range(required_pages):
		if problem_start + k - 1 >= i:
			problem_end = i
		else:
			problem_end = problem_start + k - 1
		if page in range(problem_start,problem_end+1):
			# print(str(page) +": "+ str(problem_start) +" "+ str(problem_end))
			result += 1
		page += 1
		problem_start = problem_end + 1

print(result)


'''
 5  3
4	2	6	1	10
1	1	1	1	1
2	2	2		2
3		3		3
--------------------
4		4		4
		5		5
		6		6


'''