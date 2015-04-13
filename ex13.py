from sys import argv
print argv
script, first, second, third = argv

print "The script is classed:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

script, first, second= argv 
name_who = raw_input("who are you?") 
print "how do you do!", name_who 
first = raw_input() 
print "let's hang out", second 
second = raw_input() 