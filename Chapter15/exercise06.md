Suppose you have a data set of survey results where respondents can optionally give their age. Missing values are read in as None. Here is a function that computes the average age from that list:
```python
from typing import List

def average(values: List[float]) -> float:
    """Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0  # The number of values seen so far.
    total = 0  # The sum of the values seen so far.
    for value in values:
        if value is not None:
            total += value

        count += 1

    return total / count
```
Unfortunately it does not work as expected:

```python
>>> import test_average
>>> test_average.average([None, 30, 20])
16.666666666666668
```
Using unittest, write a set of tests for function average in a module called test_average.py. The tests should cover cases involving lists with and without missing values.

Modify function average so it correctly handles missing values and passes all of your tests.

### Answer :
```python
from typing import List
import unittest

def average(values: List[float]) -> float:
    """Return the average of the numbers in values.  Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0  # The number of values seen so far.
    total = 0  # The sum of the values seen so far.

    for value in values:

        if value is not None and value != 0:
            total += value
            # The count parameter increments is run 3 times instead of two, this is the correct version, it was wrong ident !
            count += 1

    try:
        return total / count
    except ZeroDivisionError:
        return 0

class TestIfSorted(unittest.TestCase):

    def testingListWithNoneValues(self):
        argument = average([None, 20, 30])
        expected = 25
        self.assertEquals(argument,expected,"Testing list with None values")
    
    def testingListWithNoNoneValues(self):
        argument = average([20, 30])
        expected = 25
        self.assertEquals(argument,expected,"Testing list without None values")
    
    def testingTheListContainsZero(self):
        argument = average([20, 30, 0])
        expected = 25
        self.assertEquals(argument,expected,"Testing list contains 0")
        pass
    
    def testingTheListIsJustZero(self):
        argument = average([0])
        expected = 0
        self.assertEquals(argument,expected,"Testing list contains 0")
        pass

unittest.main()
```