"""
Provide services for automatically extending lists.

inflist provides a list subclass to allow for automagically extending lists.
InfList represents a list that allows extending indefinitely without any fuss.
Indexing a non-assigned thing works as expected; first, normal lookup is tried
like normal lists. If that fails, then a default value is returned, or
optionally an exception is raised.

Currently setting a value outside the currently existing list just appends, so,
for example,
 >>> li = InfList()
 >>> li[200] = 1
 >>> print li
 [1]

is expected behaviour (for now). I can't really see a use beyond simply setting
the next value, so this is a low priority "bug".

"""

class InfList(list):
    """Represent an infinite list."""

    def __init__(self, *args, **kwds):
        """
        Initialise the list.

        Same constructor as stock Python list(), except with the addition of
        of the default keyword argument.

        The default argument sets the default value to get if an uninitialised
        value is accessed. If it is None, then IndexError is raised instead.
        It can be changed on an instance via setting of self.default.
        
        """
        self.default = kwds.pop('default', 0)
        super(InfList, self).__init__(*args, **kwds)

    def __getitem__(self, index):
        try:
            return super(InfList, self).__getitem__(index)
        except IndexError:
            if self.default == None:
                raise
            return self.default

    def __setitem__(self, index, value):
        try:
            super(InfList, self).__setitem__(index, value)
        except IndexError:
            self.append(value)

    def __eq__(self, other):
        """
        Override the default list comparison operation to a more "natural" one.

        Two lists (infinite or not) are equal if an infinite list can be
        extended to a list equal to the other. For example,

         >>> li1, li2 = InfList(), range(3)
         >>> li1 == li2
         False
         >>> li2 = [0] * 3
         >>> li1 == li2
         True

        """
        if super(InfList, self).__eq__(other):
            return True
        else:
            lself, lother = len(self), len(other)
            if lself < lother and self[:lother] == other:
                return True
            else:
                return False

    def __getslice__(self, i, j):
        if self.default == None:
            return super(InfList, self).__getslice__(i, j)
        else:
            retval = InfList(default=self.default)
            while i < j:
                retval.append(self[i])
                i += 1
            return retval
