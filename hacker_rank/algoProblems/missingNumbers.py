a=int(input())
list_a = input().split()
b=int(input())
list_b = input().split()
afreq={}
bfreq={}
final_list = []



for i in list_a:
	if i in afreq:
		afreq[i] = afreq[i] + 1
	if i not in afreq:
		afreq[i] = 1

for i in list_b:
	if i in bfreq:
		bfreq[i] = bfreq[i] + 1
	if i not in bfreq:
		bfreq[i] = 1

for i in set(list_b):
	if afreq[i] != bfreq[i]:
		final_list.append(i)
# list_a.sort()
# list_b.sort()
# list_length = len(list_a)
# if len(list_a) < len(list_b):
# 	list_length = list_b
# for i in list_b:
# 	if i in final_list:
# 		continue
# 	if i not in list_a:
# 		final_list.append(i)
# 	if list_b.count(i) != list_a.count(i):
# 		final_list.append(i)
final_list.sort()
print_words = ''
for i in final_list:
	print_words += str(i) + " "

print(print_words[:-1])



# https://www.hackerrank.com/challenges/missing-numbers