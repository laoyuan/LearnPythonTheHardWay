The Magic Argument Parser: modargs!
===================================

This project is a simple command line argument parser that tries to
do as much as it can dynamically so that you don't have to specify
options and arguments with tons of code, and instead just write a
couple of modules with specially formatted functions.  It does this
with magic, by inspecting the modules you tell it to load and looking
for the right functions.

You can learn how to use it by looking at the following files:

* tests/commands.py -- This is a simple demo command file.
* tests/loadme.py -- This one can be loaded dynamically.
* examples/simple -- This just loads tests.commands.
* examples/modular -- This loads command modules on the fly based on the first argument.

The gist of how you use it is you make a function like this:

    def blahblah\_command(port=100):
       """
       Test command that shows how to do some common options types.
       """
       assert port == 200, "Expecting to get 200 but you passed: %r" % port
       print "PORT IS", port


You then write your bin script to load this module and process
the sys.argv like this (found in "examples/simple"):

    from modargs import args
    from tests import commands
    import sys

    args.parse_and_run_command(sys.argv[1:], commands, default_command="test")

It will then parse the command line, find out what command in the "commands"
module is requested, and run it with the remaining arguments passed as
key=value function parameters.

The parser will also convert numbers and True/False values to their appropriate
types.  You can also set defaults in the function call and they'll be accepted
if the user doesn't give a option.

Modular Commands
===============

You may want a command line tool similar to git where the commands come from
some sort of "sub-command" like this:

  tool machine add --port 2000
  tool server start --host stuff.com

In this case you can use the "args.load\_module" function to just load the
module that's in the first argument, pop it off, then run everything like
normal.  Here's the script "examples/modular" that does this:

    from modargs import args
    import sys

    if len(sys.argv) < 2:
    print "USAGE: modular [loadme | commands] command <options>"
    sys.exit(1)

    base = sys.argv.pop(1)
    commands = args.load_module("tests." + base)

    if not commands:
        print "ERROR: Unsupported base command: %s. Try loadme or commands." % base
        sys.exit(1)

    args.parse_and_run_command(sys.argv[1:], commands, default_command="blahblah")


TODO
====

Right now, since I extraced this from Lamson, the module does some bad things
like call sys.exit(1) and it makes certain decisions about options like they
can have any number of dashes.  This will change as people complain about it.


Contributing
============

modargs itself has no external dependencies, but if you want to contribute to the project you will need
to install two libraries:

 * mock
 * nose

For your convenience there is a ``dev-requirements.txt`` and you can just run:

    pip install -r dev-requirements.txt

to install them.
