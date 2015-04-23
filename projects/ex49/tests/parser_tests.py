from nose.tools import *
from ex49 import parser
from ex48 import lexicon


def test_peek():
    word_list = lexicon.scan("open the door")
    assert_equal(parser.peek(word_list), 'verb')

def test_match():
    word_list = lexicon.scan("open the door")
    assert_equal(parser.match(word_list, 'verb'), ('verb', 'open'))
    assert_equal(word_list, [('stop', 'the'), ('noun', 'door')])

def test_skip():
    word_list = lexicon.scan("the door")
    parser.skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'door')])

def test_verb():
    word_list = lexicon.scan("now open the door")
    result = parser.parse_verb(word_list)
    assert_equal(result, ('verb', 'open'))

def test_object():
    word_list = lexicon.scan("the door")
    result = parser.parse_object(word_list)
    assert_equal(result, ('noun', 'door'))

    word_list = lexicon.scan("now east")
    result = parser.parse_object(word_list)
    assert_equal(result, ('direction', 'east'))


def test_sentence():
    word_list = lexicon.scan("open the door")
    result1 = parser.parse_sentence(word_list)
    result2 = parser.parse_subject(lexicon.scan("open the door"), ('noun', 'player'))
    assert_equal(result1.subject, result2.subject)
    assert_equal(result1.verb, result2.verb)
    assert_equal(result1.object, result2.object)

    word_list = lexicon.scan("now bear go east")
    result1 = parser.parse_sentence(word_list)
    result2 = parser.parse_subject(lexicon.scan("go east"), ('noun', 'bear'))
    assert_equal(result1.subject, result2.subject)
    assert_equal(result1.verb, result2.verb)
    assert_equal(result1.object, result2.object)

def test_errors():
    word_list = lexicon.scan("bear go east")
    assert_raises(Exception, parser.parse_verb, word_list)
    word_list = lexicon.scan("go east")
    assert_raises(Exception, parser.parse_object, word_list)
    word_list = lexicon.scan("east")
    assert_raises(Exception, parser.parse_sentence, word_list)






