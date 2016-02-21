a = int(raw_input())
list_of_names = []

for i in range(a):
	list_of_names.append(list(raw_input().strip()))
	list_of_names[i].sort()

groups = []
unique_count = 0
for i in range(len(list_of_names)):
	if list_of_names[i] not in groups:
		groups.append(list_of_names[i])
		unique_count +=1

print unique_count
