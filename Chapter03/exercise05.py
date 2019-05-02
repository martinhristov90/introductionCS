#Following the function design recipe, define a function that has one parameter, 
#a distance in kilometers, and returns the distance in miles. (There are 1.6 kilometers per mile.)

def kilometerToMiles(arg1: int) -> float:
    """
        The function takes one argument arg1, the distance in kilometers, as a result it returns the distance in miles.
        Example :
        >>> kilometerToMiles(100)
        160.0
        >>> 
    """
    return arg1 * 1.6
