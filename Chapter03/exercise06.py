#Following the function design recipe, define a function that has three parameters, 
#grades between 0 and 100 inclusive, and returns the average of those grades.

def avarageGrade(arg1: float, arg2:float, arg3:float) -> float:
    """
        The function takes three arguments, it sums them up and results in the avarage value of the three.
        Example :
            >>> avarageGrade(3,3,3)
            3.0
            >>> avarageGrade(3,4,3)
            3.3333333333333335
            >>> 

    """
    return (arg1+arg2+arg3)/3

