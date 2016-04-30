# Author: HarshilPatel
# harshil912@gmail.com
# Python3
# Simple aray sum
# https://www.hackerrank.com/challenges/simple-array-sum

input_size = input()
elements = input().split()
# Converting to integer
for i in range(len(elements)):
	elements[i] = int(elements[i])

# calculating

result = 0
for i in elements:
	result = result + i
print(result)
