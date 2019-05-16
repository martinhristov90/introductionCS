### What happens if the functions to find the two smallest values in a list are passed a list of length one? What should happen, and why? How about length zero? Modify one of the docstrings to describe what happens.

> Answer : The function should return an error, that at least two values are needed in the list,if lenght is zero, an error should be returned as well.

```python

import doctest
    
def find_two_smallest (inList) :
    """
    (list) -> tuple
    Returns the two smallest numbers in the list passed as argument to the funciton.
    >>> find_two_smallest([5,6,33,4,5,6])
    (4, 5)
    >>> find_two_smallest([1])
    'The list should contain at least two values'
    """
    if len(inList) < 2:
        return 'The list should contain at least two values'
        
    return(sorted(inList)[0],sorted(inList)[1]) 

doctest.testmod()
print(find_two_smallest([1,2]))
# Result : (1, 2)
print(find_two_smallest([0,0]))
# Result: (0,0)
print(find_two_smallest([1]))
# Result: (1,1)

```