# symmetric point math
# harshil912@gmail.com
# py3
import math
for i in range(int(input())):
	points = [int(x) for x in input().strip().split()]
	px,py,qx,qy = points[0],points[1],points[2],points[3]
	x_difference = int(math.fabs(px-qx))
	y_difference = int(math.fabs(py-qy))
	print( str(x_difference + qx) +" "+ str(y_difference + qy))