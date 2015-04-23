from nose.tools import *
import os
from modargs import args
from mock import *
import sys
from tests import commands


def test_match():
    tokens = [["word", "test"],["int", 1]]
    assert args.match(tokens, "word") == "test", "Wrong word on match."
    assert args.match(tokens) == 1, "Wrong int on match."

    assert len(tokens) == 0, "There should be nothing in the array after matching."


@raises(args.ArgumentError)
def test_match_fails():
    tokens = [["word", "test"],["int", 1]]
    args.match(tokens, "string")

def test_peek():
    tokens = [["word", "test"],["int", 1]]
    assert args.peek(tokens, "word"), "There should be a word."
    assert len(tokens) == 2, "Args should not go down after peek."
    args.match(tokens, "word")

    assert args.peek(tokens, "int"), "There should be an int."
    assert not args.peek(tokens, "option"), "There should not be an option."
    args.match(tokens, "int")

@raises(args.ArgumentError)
def test_peek_fails():
    tokens = []
    args.peek(tokens, 'string')

def test_determine_kwargs():
    kw = args.determine_kwargs(commands.test_command)
    assert kw['pid']

def test_tokenize():
    tokens = args.tokenize(['test', '--num', '1', '--help', '--stuff', 'The remainder.'])
    assert args.match(tokens, 'word')
    assert args.match(tokens, 'option')
    assert args.match(tokens, 'int')
    assert args.match(tokens, 'option')
    assert args.match(tokens, 'option')
    assert args.match(tokens, 'string')

    # test a condition where there is a remainder that's not identified
    tokens = args.tokenize(['stop', '--pid', 'run/log.pid'])
    assert tokens
    assert args.match(tokens, 'word')
    assert args.match(tokens, 'option')
    assert args.match(tokens, 'string')


def test_parse():
    command, options = args.parse(['test', '--num', '1', '--help', '--stuff', 'The remainder.', '--tail'])
    assert command, "There should be a command."
    assert options, "There should be options."

    assert command == "test", "command should be test"
    assert options["num"] == 1, "num option wrong"
    assert options["help"] == True, "help should be true"
    assert options["stuff"] == 'The remainder.', "stuff should a string"
    assert options['tail'] == True, "There should be a True tail."

    command2, options = args.parse(['--num', '1', '--help', '--stuff', 'The remainder.'])
    assert not command2, "There should NOT be a command."
    assert options, "There should be options."
    assert options["num"] == 1, "num option wrong"
    assert options["help"] == True, "help should be true"
    assert options["stuff"] == 'The remainder.', "stuff should a string"

    _, options = args.parse(['--foo', 'True', '--bar', 'False'])
    assert options['foo']
    assert not options['bar']

    _, options = args.parse(['--foo', 'true', '--bar', 'false'])
    assert options['foo']
    assert not options['bar']

    _, options = args.parse(['--foo', 'yes', '--bar', 'no'])
    assert options['foo']
    assert not options['bar']


def test_defaults():
    command, options = args.parse(['test', '--num', '1', '--help', '--stuff', 'The remainder.'])
    args.ensure_defaults(options, {'num': 2, 'help': True, 'stuff': None})
    assert options['help'] == True
    assert options['num'] == 1

    command, options = args.parse(['test', '--num', '1', '--help', '--stuff', 'The remainder.'])
    args.ensure_defaults(options, {'num': 2, 'extras': 3, 'help': None, 
                                   'stuff': None})
    assert options['extras'] == 3
    assert options['num'] == 1


    assert_raises(args.ArgumentError,
                  args.ensure_defaults,
                  options, {'num': 2, 'extras': 3, 'help': None, 'TRAILING': None})

    assert_raises(args.ArgumentError,
                  args.ensure_defaults,
                  options, {'num': 2, 'extras': 3, 'help': None, 'bad': None})

def test_help_for_command():
    assert args.help_for_command(commands, "test")
    assert not args.help_for_command(commands, "badcommand")

def test_available_help():
    assert args.available_help(commands)

def test_available_commands():
    assert args.available_commands(commands).index('test') >= 0, 'no help command'

def test_trailing():
    command, options = args.parse(['test', '--num', '1', '--', 'Trailing 1', 'Trailing 2'])
    expected = ['Trailing 1', 'Trailing 2']
    assert command == 'test'
    assert options['TRAILING']
    for e in expected: assert e in options['TRAILING']

    # test with a corner case of a switch option before trailing
    command, options = args.parse(['test', '--num', '1', '--switch', '--', 'Trailing 1', 'Trailing 2'])
    for e in expected: assert e in options['TRAILING']


@raises(SystemExit)
def test_invalid_options():
    args.parse_and_run_command(['test', '-foobar'], commands)

def test_no_command_or_default():
    args.parse_and_run_command([], commands,
                                      default_command=None,
                                      exit_on_error=False)

def test_load_a_module():
    loaded_module = args.load_module("tests.loadme")
    args.parse_and_run_command(['blahblah', '-port', '200'], loaded_module)

def test_mixed_type_args():
    fn = args.function_for(commands, "mixed_type")
    kwargs = args.determine_kwargs(fn)
    assert kwargs['kwfoo'] == 5
    assert kwargs['kwbaz'] == 'ok'

def test_multiple_kwargs():
    options = args.parse(['testmanykwargs', '-foo', 'bar', '-foo', 'baz'])[1]
    assert options['foo'] == ['bar', 'baz']
    options = args.parse(['testmanykwargs', '-foo', 'bar', '-foo', 'baz', '-foo', 'bag'])[1]
    assert options['foo'] == ['bar', 'baz', 'bag']

def test_kwdocs():
    fn = args.function_for(commands, "documented")
    kwdocs = args.determine_kwdocs(fn)
    assert kwdocs['port'] == "The TCP port on which to connect"
    assert kwdocs['host'] == "The host to run as"
    assert kwdocs['chroot'] == "TODO what should happen here.."
    assert kwdocs['chdir'] is None
    assert kwdocs['kwargs'] == "Other unspecified args to be passed to another command."

def test_help():
    help_text = args.help_text('modargs', commands)
    assert "Available commands for modargs" in help_text
    assert "documented" in help_text
    assert "modargs help -on" in help_text

def test_help_on_command():
    fn = args.function_for(commands, "documented")
    help_text = args.help_text('modargs', commands, on="documented")
    assert "Help for 'modargs documented'" in help_text
    assert "This is a very important command" in help_text
    assert "port - The TCP port on which to connect" in help_text
    assert "e.g. 'modargs documented --port 8825'" in help_text
    assert "Keyword Arguments" in help_text

def test_cli_options():
    args.parse_and_run_command(['clioptions', '-kwfoo', '7'], commands)
