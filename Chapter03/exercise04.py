#Following the function design recipe, define a function that has two parameters, both of which are numbers, 
#and returns the absolute value of the difference of the two. Hint: Call built-in function abs.

def diffNumAbs(arg1: int, arg2: int) -> int:
    """
        The function takes two arguments arg1 and arg2, both int.
        The function as result returns the absolute value of the difference of the two numbers feeded as arguments.
        Example : 
        >>> diffNumAbs(4,6)
        2
        >>> 
    """
    res = arg1 - arg2
    return abs(res)

