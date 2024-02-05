# getPower  base = 5 and exponent = 4 
#  -> the value 5 to the power of 4 = 5*5*5*5 = 625

base = 5
exponent = 4
result = 1
counter = 0

if exponent == 0:
	result = 1

else:
	while counter < exponent:
		result *= base
		counter += 1

print (f" {base} to the power of {exponent} = {result}")
