#Following the function design recipe, define a function that has four parameters, all of them grades between 0 and 100 inclusive, 
#and returns the average of the best 3 of those grades. Hint: Call the function that you defined in the previous exercise.

def avarageOfBest3(arg1: float, arg2:float, arg3:float, arg4:float) -> float:
    """
        The function takes four arguments, it returns the avarage value of the best three grades.
        Example :
        >>> avarageOfBest3(3,4,4,5)
        4.333333333333333
        >>> 
    """
    """
    grades = [arg1,arg2,arg3,arg4]

    grades = sorted(grades)

    grades = grades[-3:]

    sum = 0

    for i in grades : 

        sum = sum + i
    
    return sum/3
    """
    minGrade = min(arg1,arg2,arg3,arg4)
    sumOfThreeGrades = ( arg1 + arg2 + arg3 + arg4 ) - minGrade
    return sumOfThreeGrades / 3




