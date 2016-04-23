# Python 3
# Author: harshil912@gmail.com
# Get Prime Numbers between 2 numbers
import time
while True:
	a = input('(Prime Numbers)Enter space seperated 2 numbers:  ')
	if a in ['no','nah','exit','done','']:
		print("Exiting Program")
		break
	elif len(a.split()) < 2:
		break
	else:
		a = a.split()
	start = time.time()
	b = int(a[1])
	a = int(a[0])
	result = []
	for i in range(a,b):
		for j in range(2,i):
			if i%j == 0:
				break
		else:
			result.append(i)
	final_result = ''
	for i in result:
		final_result += " " + str(i)
	print(final_result)
	end = time.time()
	print("Time Taken:  " + str(end-start))