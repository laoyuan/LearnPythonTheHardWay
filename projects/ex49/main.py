from ex49 import parser
from ex48 import lexicon
from ex49.parser import Parser_c

p = Parser_c()
word_list = lexicon.scan("open the fucking door")
result = p.parse_sentence(word_list)

print result.subject, result.verb, result.object 
