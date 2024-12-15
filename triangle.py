def area(a, h):
    """
    Takes the base length and height of a triangle and returns its area

    Parameters:
    a (float): - base length of the triangle
    h (float): - height of the triangle

    Returns:
    float: - area of the triangle

    Example usage:
    >>> area(2, 3)
    3
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Takes the lengths of the sides of a triangle and returns its perimeter

    Parameters:
    a (float): - length of a side of the triangle
    b (float): - length of a side of the triangle
    c (float): - length of a side of the triangle

    Returns:
    float: - perimeter of the triangle

    Example usage:
    >>> perimeter(1, 2, 3)
    6
    """
    return a + b + c
