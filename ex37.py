#coding: utf-8

"""
and
as
assert
break
class
continue
def
del
elif
else
except
exec
finally
for
from
global
if
import
in
is
lambda
not
or
pass
print
raise
return
try
while
with
yield
"""

print "hoho %s %%" % 'a'

print "\a \b \f \r \v \n"

print None
print 17 / 4
print 17.0 / 4
print 17 / 4.0

print 17 // 4
print 17.0 // 4
print 17 // 4.0





def f(): pass

a = {}
b = {}
print a is b #False
print a == b #True

exec 'print a'

file = open("ex1.py")
data = file.read()
print data, "\n111\n\n"


try:
    data = file.read()
finally:
    file.close()

print data

with open("ex2.py") as file:
    data = file.read()
print data
 
class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, type, value, trace):
        print "In __exit__()"
 
    
def get_sample():
    return Sample()
 
 
with get_sample() as sample:
    print "sample:", sample




