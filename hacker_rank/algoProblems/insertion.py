# Author: HarshilPatel
# harshil912@gmail.com
# Python3
a = int(input())
b = [int(x) for x in input().split()]

to_sort = b[a-1]
sorted = False
print(to_sort)
ref_array = list(range(a))
ref_array.reverse()

for j in ref_array:
	# j = a-i
	if to_sort < b[j-1]:
		b[j] = b[j-1]
		temp = ''
		for i in b:
			temp += str(i) + " "
		print(temp[:-1])
	if to_sort > b[j-1]:
		b[j-1] = to_sort
		print(to_sort)
		temp = ''
		for i in b:
			temp += str(i) + " "
		print(temp[:-1])
		break