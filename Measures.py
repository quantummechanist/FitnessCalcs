#!python3
""" Module that contains basic measurement types for making comparisons and conversions"""

class Measure:
    """ A normalized mass measurement container based on SI units """

    def __typecheck__(self, other):
        if not isinstance(self, other):
            raise TypeError("Cannot compare two disimilar types of measure")

    def __init__(self, val):
        self.native = val
        self.val = None

    def __eq__(self, other):
        self.__typecheck__(other)
        return self.val == other.val

    def __gt__(self, other):
        self.__typecheck__(other)
        return self.val > other.val

    def __lt__(self, other):
        self.__typecheck__(other)
        return other.__gt__(self)

    def __ge__(self, other):
        self.__typecheck__(other)
        return self.val >= other.val

    def __le__(self, other):
        self.__typecheck__(other)
        return other.__ge__(self)

    def __ne__(self, other):
        self.__typecheck__(other)
        return self.val != other.val

    def __call__(self):
        return self.val

class Mass(Measure):
    """ A abstract container for SI-referenced measurements"""
    def __init__(self, val):
        super().__init__(val)


class Pound(Mass):
    """ A mass measure taking pounds into SI internally"""
    def __init__(self, val):
        super().__init__(val)

        self.val = val / 0.454

class Gram(Mass):
    """Gram in SI norm units"""
    def __init__(self, val):
        super().__init__(val)
        self.val = val / 1000

class Distance(Measure):
    """Distance is an abstract class of Measure"""
    def __init__(self, val):
        super().__init__(val)

class Meter(Distance):
    """Meter is an SI class of distance"""
    def __init__(self, val):
        super().__init__(val)
        self.val = val

class Inch(Distance):
    """Inch in SI units"""
    def __init__(self, val):
        super().__init__(val)
        self.val = 0.025 * val
