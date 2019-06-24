### The following function is broken. The docstring describes what it’s supposed to do:
```python
def find_min_max(values: list):
    """Print the minimum and maximum value from values.
    """

    min = values[0]
    max = values[-1]

    for value in values:
        if value > max:
            max = value
        if value < min:
            min = value

    print('The minimum value is {0}'.format(min))
    print('The maximum value is {0}'.format(max))

# Both values were declared as None type, you cannot compare "None" type with "int" type, also two random values need to be picked, so the rest of the values can compare against them.

find_min_max([2,10,10,1,-1,-4,5,2,3])

# Result :
# The minimum value is -4
# The maximum value is 10
```