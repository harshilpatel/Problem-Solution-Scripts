# Fibonacci series
import time

def main(a):
	f0 = 0
	f1 = 1
	result = '0 1 '
	for i in range(a):
		temp = f1 + f0
		f0 ,f1 = f1, temp
		result += str(temp) + ' '
	return result


if __name__ == '__main__':
	print "Welcome to fib series"
	a = int(raw_input("Enter the range to print[One integer]"))
	print main(a)