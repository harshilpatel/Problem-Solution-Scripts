[n,m] = [int(i) for i in raw_input().split()]

seq = {}
for i in range(m):
	[a,b,c] = [int(i) for i in raw_input().split()]
	for j in xrange(a-1,b):
		if seq.get(j):
			seq[j] += c
		else:
			seq[j] = c

print max(seq.values())