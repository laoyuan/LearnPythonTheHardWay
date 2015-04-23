"""
A simple test command set for the unit tests and as examples of doing different
things.
"""


def blahblah_command(port=100):
    """
    Test command that shows how to do some common options types.
    """
    assert port == 200, "Expecting to get 200 but you passed: %r" % port
    print "PORT IS", port
