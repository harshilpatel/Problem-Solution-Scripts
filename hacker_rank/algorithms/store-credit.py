# https://code.google.com/codejam/contest/351101/dashboard#s=p0

output = ""
for test_case in range(int(raw_input())):
	c = int(raw_input())
	items = int(raw_input())
	cost = [int(i) for i in raw_input().split()]

	a = 0
	b = 0

	for i in range(items):
		if not a and not b:
			for j in range(items):
				if i+j == c:
					a,b = i,j
					break

	if a>b:
		a,b = b,a

	output += "Case #%s: %s %s\n"%(test_case+1, a,b)

print output


