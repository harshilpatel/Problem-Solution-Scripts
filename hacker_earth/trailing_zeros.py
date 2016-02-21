a= int(input())
fact = a
for i in range(1,a):
	fact *= i
print fact

fact_string = str(fact)
count = 0
for i in reversed(range(len(fact_string))):
	if fact_string[i] == "0":
		count +=1
	else:
		break

print str(count)