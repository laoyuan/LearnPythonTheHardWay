formatter = "%r %r %r %r"
formatter_s = "%s %s %s %s"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

print formatter_s % (1, 2, 3, 4)
print formatter_s % ("one", "two", "three", "four")
print formatter_s % (True, False, False, True)
print formatter_s % (formatter, formatter, formatter, formatter)
print formatter_s % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)



