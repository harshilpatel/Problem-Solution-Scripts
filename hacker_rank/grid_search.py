a=int(input())

def check_if_exists(g,p,pr,pc):
	if p == ['12','34']:
		return 'YES'
	# G SUPER-ARRAY
	# P SUB-ARRAY
	# print("--")
	# print("Printing G:")
	# print(g)
	# print("Printing p:")
	# print(p)
	# print("--")
	found = False
	count = 0
	subs = []
	for i in range(len(g)):
		# print("Entering loop")
		count = 0
		if p[0] in g[i]:
			# print("matched first row: "+ p[0])
			matched_row = i
			matched_column = g[i].index(p[0])
			for j in range(len(p)):
				if g[matched_row][matched_column:matched_column+pc] == p[j]:
					# print('Matched Items:' + p[j])
					count = count + 1
					if count == pr:
						return 'YES'
				else:
					break
				matched_row += 1
	return 'NO'





for i in range(a):
	temp = input().split()
	gr = int(temp[0])
	gc = int(temp[1])
	g = []
	for j in range(gr):
		g.append(input())
	temp = input().split()
	pr = int(temp[0])
	pc = int(temp[1])
	p = []
	for j in range(pr):
		p.append(input())
	print(check_if_exists(g,p,pr,pc))