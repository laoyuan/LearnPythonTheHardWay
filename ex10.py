tabby_cat = "	I'm tabbed in."
persian_cat = "I'm split\non a line. %r" % tabby_cat

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

backslash_cat = "I'm \\ a \\ cat. %r" % fat_cat



print tabby_cat
print persian_cat
print backslash_cat
print fat_cat