import math
c = int(raw_input())
a = int(raw_input())
b = c/2
result = (b*b + c*c - a*a) / 2*b*c
result = math.acos(result)
# result = result.degrees(result)
print result