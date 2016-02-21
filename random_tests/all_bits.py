# 

a = [0,1,2,3,4,5]
def binary(n):
	global a
	if n<1:
		print(n)
	else:
		a[n-1] = 0
		binary(n-1)
		a[n-1] = 1
		binary(n-1)




while "1" == '1':
	abcd = int(input())
	binary(abcd)