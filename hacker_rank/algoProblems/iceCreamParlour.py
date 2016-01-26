test_cases = int(input())

for i in range(test_cases):
	m = int(input())
	n = int(input())
	items = [int(x) for x in input().split()]
	found = False
	for i in range(len(items)):
		if found == True:
			break
		for j in range(len(items)):
			if i==j:
				continue
			if items[i] + items[j] == m:
				print(str(i+1) + " " + str(j+1))
				found = True



'''
Sunny and Johnny together have M dollars they want to spend on ice cream. The parlor offers N flavors, and they want to choose two flavors so that they end up spending the whole amount.

You are given the cost of these flavors. The cost of the ith flavor is denoted by ci. You have to display the indices of the two flavors whose sum is M.

Input Format

The first line of the input contains T; T test cases follow. 
Each test case follows the format detailed below: The first line contains M. The second line contains N. The third line contains N space-separated integers denoting the price of each flavor. Here, the ith integer denotes ci.

Output Format

Output two integers, each of which is a valid index of a flavor. The lower index must be printed first. Indices are indexed from 1 to N.

Constraints

1≤T≤50 
2≤M≤10000 
2≤N≤10000 
1≤ci ≤10000,where i∈[1,N] 
The prices of any two items may be the same and each test case has a unique solution.
'''


