class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self, ls=[]):
        """ initialization of your representation """
        self.ls = ls

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.k = k
        self.v = v
        self.ls.extend((k, v))

    def getval(self, k):
        """ k, immutable object  """
        self.k = k
        # if k % 2 != 0:        # added those 2 lines after the assignment but I think they work
        #     raise KeyError
        if self.ls.count(k) > 1:
            k += 1

        return self.ls[self.ls.index(k) + 1]

    def delete(self, k):
        """ k, immutable object """
        try:
            self.k = k
            del self.ls[self.ls.index(k) + 1]
            self.ls.remove(k)
        except:
            raise KeyError
