 #we check if the given postcode is on the list

postcode = 8000
sortedPostcodeList = [1000, 8000, 1250, 4000]
if postcode not in sortedPostcodeList:
	print(postcode , " nicht in der Liste")
else:
	for code in sortedPostcodeList:
		if code == postcode:
			print(postcode, " ist in der Liste")
			break