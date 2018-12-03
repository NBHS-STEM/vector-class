import math
import numpy as np


class Vector:
    """
    A simple n-dimensional vector class. Supports addition, subtraction, L2 Norm,
    dot product and scalar multiplication
    """

    def __init__(self, *components):
        self.components = np.array(components)

    def __repr__(self):
        return f'Vector{tuple(self.components)}'

    def __eq__(self, other):
        return self.components == other.components

    def __abs__(self):
        """ Returns L2 (Euclidean) Norm """
        return math.sqrt(sum(self.components ** 2))

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        """ Returns component-wise sum as a Vector """
        return self + other

    def __mul__(self, other):
        """ Returns dot product """
        return sum(self * other)

    def __rmul__(self, other):
        """ Supports (left) scalar multiplication """
        return other * self

    def __neg__(self):
        """ Unary minus support """
        return Vector(* -self.components)

    def __sub__(self, other):
        """ Returns component-wise difference as a Vector """
        return self - other


def angle(a: Vector, b: Vector, degrees=True) -> float:
    """ Returns the angle between two Vectors in degrees unless degrees=False """
    a = math.acos((a*b)/(abs(a)*abs(b)))
    if degrees:
        return math.degrees(a)
    else:
        return a


