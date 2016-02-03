test_cases = int(input())

for i in range(test_cases):
	a = int(input())
	firstArray = [int(x) for x in input().split()]
	contigous = non_contigous =  0
	for i in firstArray:
		if i > 0:
			non_contigous += i
	if non_contigous == 0:
		non_contigous = max(firstArray)
	range_start = 0
	range_end = a
	stays_max = True
	# non_contigous = sum(firstArray)
	count = 0
	end_looks_good = start_looks_good = False
	# while stays_max == True:
	# 	if range_start < a and range_end > 0:
	# 		pass
	# 	else:
	# 		stays_max = False
	# 	contigous = sum(firstArray[range_start:range_end])
	# 	if sum(firstArray[range_start:range_end-1]) > contigous:
	# 		range_end -=1
	# 		contigous = sum(firstArray[range_start:range_end])
	# 	else:
	# 		end_looks_good = True
	# 	if sum(firstArray[range_start+1:range_end]) > contigous:
	# 		range_start +=1
	# 		contigous = sum(firstArray[range_start:range_end])
	# 	else:
	# 		start_looks_good = True
	# 	if start_looks_good and end_looks_good:
	# 		stays_max = False
		


	for i in range(a):
		for j in range(i):
			if i == j == 0:
				continue
			for k in firstArray[j:i+1]:
				sum_of_elements +=k
			# sum_of_elements = sum(firstArray[j:i+1])
			if sum_of_elements > non_contigous:
				non_contigous = sum_of_elements

	print( str(contigous) + " " + str(non_contigous)) 