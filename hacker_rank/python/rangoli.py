alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a = int(input())
temp_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
temp_range = list(range(a))
temp_range.reverse()
count = ((a-1)*4)+1
for i in temp_range[:-1]:
	final_string = ''
	temp_string2 = '-'.join(temp_string[i:a])[::-1][:-1] +'-'.join(temp_string[i:a])
	final_string = "-"*int((count-len(temp_string2))/2)
	print( final_string + temp_string2 + final_string  )
	# temp_string.remove(temp_string[0])

# temp_string = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(a):
	final_string = ''
	temp_string2 = '-'.join(temp_string[i:a])[::-1][:-1] +'-'.join(temp_string[i:a])
	final_string = "-"*int((count-len(temp_string2))/2)
	print(final_string+  temp_string2 + final_string)
	# temp_string.remove(temp_string[0])
	