
def cc(times, add):
	i = 0
	num = 0
	numbers = []

	for i in range(times):
		print "At the top i is %d" % num
		numbers.append(num)
		num = num + add
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % num

	print "The numbers: "
	for num in numbers:
	    print num


cc(3, 2)


