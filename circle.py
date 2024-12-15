import math


def area(r):
    """
    takes the radius of a circle and returns its area

    parameters:
    r (float): - radius of the circle

    return value:
    float: - area of the circle

    example usage:
    >>> area(1)
    3.141592
    """
    return math.pi * r * r


def perimeter(r):
    """
    takes the radius of a circle and returns its circumference

    parameters:
    r (float): - radius of the circle

    return value:
    float: - circumference of the circle

    example usage:
    >>> perimeter(1)
    6.283184
    """
    return 2 * math.pi * r
