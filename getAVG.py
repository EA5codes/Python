def avg(numberList):
    total = 0
    counter =0
    while counter < len(numberList):
        total += numberList[counter]
        counter += 1
        return total / counter

list = [30, 15, 40, 2, 21, 90, 12]
result = avg(list)
print(result)
print(len(list))
