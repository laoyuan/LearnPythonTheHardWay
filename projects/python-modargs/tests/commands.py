"""
A simple test command set for the unit tests and as examples of doing different
things.
"""

import os

TEST_RAN=False
TEST_TRAILING=None

def test_command(port=8825, host='127.0.0.1', chroot=False,
                chdir=".", uid=False, gid=False, umask=False, pid="./run/log.pid",
               FORCE=False):
    """
    Test command that shows how to do some common options types.
    """
    # NOTE: You shouldn't be setting up globals like this, this is just for
    # unit tests.
    global TEST_RAN
    TEST_RAN=True
    print "TEST COMMAND RAN", port, host, chroot, chdir, uid, gid, umask, pid, FORCE

def trailing_command(TRAILING=['config.testing'], path=os.getcwd(), test=""):
    """
    Tests that the trailing options feature works.
    """
    # NOTE: You shouldn't be setting up globals like this, this is just for
    # unit tests.
    global TEST_TRAILING
    TEST_TRAILING = TRAILING

    print "I GOT: ", TRAILING, path, test

def documented_command(
        port=8825, # The TCP port on which to connect
        host='127.0.0.1', # The host to run as
        chroot=False, chdir=".", # TODO what should happen here..
        **mykwargs # Other unspecified args to be passed to another command.
    ):
    """
    This is a very important command that does really important stuff.
    """
    print "ok"
    return True

def mixed_type_command(foo, bar, kwfoo=5, kwbaz='ok', **kwargs):
    """Used to test that we match up the arg names and values when we start with non-kw args."""
    pass

def clioptions_command(__cli_options=False, kwfoo=5, kwbaz="ok"):
    assert __cli_options
    assert __cli_options['kwfoo'] == 7
    assert kwfoo == 7
