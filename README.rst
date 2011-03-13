dutchie-bits
============

These are simple Python modules I have written for my own personal use that
are general enough for re-use by myself and others. They are licensed under
the permissive BSD licence.

Bug reports and patches are welcome.

fpi.py
------

fpi.py is an equation solver written in Python. It uses the method of fixed
point iteration based on a user-provided script and command line parameters
to define the function to solve and various other parameters.

Hopefully the code is more or less self-documenting, check `./fpi.py --help` too.

The only requirement is a working Python implementation; only core packages
are used.

TODO
 - establish whether using decimal.Decimal is the right way to go
   (it's a pain to use with the math module)

 - add a load of docstrings

inflist.py
----------

inflist.py is a a module to provide a list subclass that acts on infinite lists
in an "intuitive" (to me) way. It was originally written to assist with
iterative algorithms that require automagic extending of lists.
