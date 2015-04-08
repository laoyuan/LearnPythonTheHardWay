animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

i = 0
for v in animals:
	print "The %dst animal is at %d and is a %s." % (i + 1, i, v)
	i += 1