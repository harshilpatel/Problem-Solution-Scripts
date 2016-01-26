min_input = int(input())
max_input = int(input())

collection= []

def check(d,l,n):
	if int(d)+int(l) == n:
		collection.append(n)
		return True
	else:
		return False

for i in range(min_input,max_input):
	item_square = i*i
	item_string = str(item_square)
	d=item_string[-len(str(i)):]
	l=item_string[:item_string.index(str(d))]
	if l == '':
		l=0
	if d == '':
		d=0
	if check(d,l,i):
		check(d,item_string[:item_string.index(str(d))+1],i)

final_string = ''

for i in collection:
	final_string = final_string + str(i) + " "
print(final_string[:-1])


