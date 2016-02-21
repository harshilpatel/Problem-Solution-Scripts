'''
Just run this FILE and have fun. Test your typing speed.
enter q to QUIT
'''

import random
import time
keep_going = True
a = list('abcdefghijklmnopqrstuvwxyz')
while keep_going:
	gen_string = ''
	for j in range(2):
		gen_stirng_length = random.randrange(1,5)
		for i in range(gen_stirng_length):
			gen_string += random.choice(a)
		if j == 0:
			gen_string += " "
	print(gen_string)
	start = time.time()
	got_string = input('Enter the above string:')
	if got_string in ['q','quit','exit','enought']:
		print("Exiting Game")
		break
	end = time.time()
	if gen_string == got_string:
		print("You did that in " +str(end-start)[:3]+ "s")
	else:
		print("Wrong string,Try next")
