# Author: HarshilPatel
# harshil912@gmail.com
# Python2

a_scores = [int(i) for i in raw_input().split()]
b_scores = [int(i) for i in raw_input().split()]

a = 0
b = 0

assert len(a_scores) == len(b_scores)

for i in range(len(a_scores)):
	if a_scores[i] > b_scores[i]:
		a+=1

	if a_scores[i] < b_scores[i]:
		b+=1

print "%s %s"%(a,b)