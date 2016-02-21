# Author: HarshilPatel
# harshil912@gmail.com
# Python3
a=int(input())
array = input().split()
array.reverse()
string = ''
for i in array:
	string += i + ' '
print(string[:-1])