#!/usr/bin/env python

import sys
import os.path
from optparse import OptionParser
import decimal

__version__ = "0.0.1"

__version_info__ = (0, 0, 1)

__copyright__ = """\
Copyright (c) 2010 Josh Holland
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law."""

__license__ = __licence__ = "GNU General Public License (GPL)"

def print_version(option, opt, value, parser):
    prog = os.path.basename(sys.argv[0])
    print "%s v%s" % (prog, __version__)
    print __copyright__
    sys.exit(0)

parser = OptionParser()
parser.add_option("-f", "--function", dest="function",
                  help="use FUNCTION in module (default \"f\")",
                  default="f")
parser.add_option("-m", "--module", dest="module",
                  help="import MODULE for user-defined variables (default \"solve\")",
                  default="solve")
parser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                  help="give more output",
                  default=False)
parser.add_option("-V", "--version", action="callback",
                  callback=print_version,
                  help="print version information")
parser.add_option("-d", "--debug", dest="debug", action="store_true",
                  help="enable debugging output",
                  default=False)

(options, args) = parser.parse_args()
