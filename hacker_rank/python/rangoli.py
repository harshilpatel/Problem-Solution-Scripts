import string

alpha = list(string.ascii_lowercase)
a = int(input())
temp_string = list(string.ascii_lowercase)
temp_range = list(range(a))
temp_range.reverse()
count = ((a-1)*4)+1
for i in temp_range[:-1]:
	final_string = ''
	temp_string2 = '-'.join(temp_string[i:a])[::-1][:-1] +'-'.join(temp_string[i:a])
	final_string = "-"*int((count-len(temp_string2))/2)
	print( final_string + temp_string2 + final_string  )
	# temp_string.remove(temp_string[0])

# temp_string = list(string.ascii_lowercase)

for i in range(a):
	final_string = ''
	temp_string2 = '-'.join(temp_string[i:a])[::-1][:-1] +'-'.join(temp_string[i:a])
	final_string = "-"*int((count-len(temp_string2))/2)
	print(final_string+  temp_string2 + final_string)
	# temp_string.remove(temp_string[0])
	