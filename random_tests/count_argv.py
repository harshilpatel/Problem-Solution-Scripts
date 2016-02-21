# harshil912@gmail.com
import sys

def main():
	result = 0
	for i in range(1,len(sys.argv)):
		result += int(i)	
	print(result)
if len(sys.argv) == 1:
	print("No Arguments Passed")
else:
	main()


# Playing with speed
import time
while True:
	test = 0
	range_value = int(input("Enter an integer:  "))
	elements = list(range(range_value))
	start = time.time()
	# for i in range(range_value):
	# 	test += i
	test = sum(elements)
	end = time.time()
	print("Result: "+ str(test)+",  Done in :" + str(end-start)+" Seconds")