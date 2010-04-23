#!/usr/bin/env python

import sys
import os.path
from optparse import OptionParser
from decimal import Decimal
import logging

__version__ = "0.0.1"

__version_info__ = (0, 0, 1)

__copyright__ = """\
Copyright (c) 2010 Josh Holland
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law."""

__license__ = __licence__ = "GNU General Public License (GPL)"

epsilon = Decimal('1e-5') # default value for epsilon

def print_version(option, opt, value, parser):
    prog = os.path.basename(sys.argv[0])
    print "%s v%s" % (prog, __version__)
    print __copyright__
    sys.exit(0)

parser = OptionParser()
parser.add_option("-V", "--version", action="callback",
                  callback=print_version,
                  help="print version information")
parser.add_option("-f", "--function", dest="function",
                  help="use FUNCTION in module (default \"f\")",
                  default="f")
parser.add_option("-m", "--module", dest="module",
                  help="import MODULE for user-defined variables (default \"solve\")",
                  default="solve")
parser.add_option("-e", "--epsilon", dest="epsilon",
                  help="set the change considered close enough (default 1e-5)")
parser.add_option("-i", "--initial", dest="initial",
                  help="set the starting value for the iteration")
parser.add_option("-v", "--verbose", dest="verbose", action="store_true",
                  help="give more output",
                  default=False)
parser.add_option("-d", "--debug", dest="debug", action="store_true",
                  help="enable debugging output",
                  default=False)

(options, args) = parser.parse_args()


log_format = "%(levelname)s: %(message)s"
if options.debug:
    logging.basicConfig(format=log_format, level=logging.DEBUG)
elif options.verbose:
    logging.basicConfig(format=log_format, level=logging.INFO)
else:
    logging.basicConfig(format=log_format)

try:
    logging.debug("Trying to import %s" % options.module)
    usermod = __import__(options.module)
except ImportError:
    logging.fatal("Couldn't import module %s." % options.module)
    logging.info("Consider specifying the --module option")
    sys.exit(1)
logging.debug("Imported %s successfully" % options.module)

try:
    logging.info("Using the function %s.%s" % (usermod.__name__, options.function))
    f = getattr(usermod, options.function)
except AttributeError:
    logging.fatal("Could not find %s in %s!" % (options.function, usermod.__name__))
    sys.exit(1)

if options.epsilon:
    logging.info("Using epsilon from command line (%s)" % options.epsilon)
    epsilon = Decimal(options.epsilon)
else:
    try:
        logging.info("Using epsilon from %s (%s)" % (usermod.__name__, usermod.epsilon))
        epsilon = usermod.epsilon
    except AttributeError:
        logging.info("No value for epsilon given, using default value %s" % epsilon)

if options.initial:
    logging.info("Using initial from command line (%s)" % options.initial)
    initial = Decimal(options.initial)
else:
    try:
        logging.info("Using initial from %s (%s)" % (usermod.__name__, usermod.initial))
        initial = usermod.initial
    except AttributeError:
        logging.fatal("No value given for initial!")
        sys.exit(1)
