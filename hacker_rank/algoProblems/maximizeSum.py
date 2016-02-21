# Author: HarshilPatel
# harshil912@gmail.com
# Python3
# import time

test_cases = int(input())
values_values = []
m_values = []
n_values = []
items_values = []
for i in range(test_cases):
	values = input().split()
	n_values.append(int(values[0]))
	m_values.append(int(values[1]))
	items_values.append([int(x) for x in input().split()])
for abcd in range(len(n_values)):
	# start_time = time.time()
	n = n_values[abcd]
	m = m_values[abcd]
	items = items_values[abcd]
	result = []
	max_value = 0

	for j in range(n):
		for k in range(j):
			if j == k:
				temp_result = items[j]%m
				if temp_result > max_value:
					max_value = temp_result
				continue
			temp_result = sum(items[k:j])%m
			if temp_result > max_value:
				max_value = temp_result
	# end_time = time.time()
	print(max_value)
	# print("Time Taken: "+ str(end_time - start_time))



''' 
You are given an array of size N and another integer M. Your target is to find the maximum value of sum of subarray modulo M.

Subarray is a continuous subset of array elements.

Note that we need to find the maximum value of (Sum of Subarray)%M , where there are N∗(N+1)/2 possible subarrays.

Input Format 
First line contains T , number of test cases to follow. Each test case consists of exactly 2 lines. First line of each test case contain 2 space separated integers N and M, size of the array and modulo value M. 
Second line contains N space separated integers representing the elements of the array.

Output Format 
For every test case output the maximum value asked above in a newline.

Constraints 
2 ≤ N ≤ 105 
1 ≤ M ≤ 1014 
1 ≤ elements of the array ≤ 1018 
2 ≤ Sum of N over all test cases ≤ 500000

Sample Input

1
5 7
3 3 9 9 5
Sample Output

6
Explanation

Max Possible Sum taking Modulo 7 is 6 , and we can get 6 by adding first and second element of the array
'''