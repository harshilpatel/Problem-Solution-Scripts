# https://www.hackerrank.com/challenges/python-string-formatting

a = int(input())
space_to_insert = ' '*len(str(bin(a))[2:])
for i in range(1,a+1):
	result = ''
	result += " "*(len(str(a))-len(str(i))) + str(i) + space_to_insert
	result += " "*(len(str(oct(a)))-len(str(oct(i)))) + str(oct(i))[2:] + space_to_insert
	result += " "*(len(str(hex(a)))-len(str(hex(i)))) + str(hex(i)).upper()[2:] + space_to_insert
	result += " "*(len(str(bin(a)))-len(str(bin(i)))) + str(bin(i))[2:] + space_to_insert
	print(result)
