result = ''
for i in range(999999999999):
	if i%10 == 0:
		result += ' ' + str(i) + "\n"
		print result 
		result = ''
		continue
	result += ' ' + str(i)
