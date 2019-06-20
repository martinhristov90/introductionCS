### Your lab partner claims to have written a function that replaces each value in a list with twice the preceding value (and the first value with 0). For example, if the list [1, 2, 3] is passed as an argument, the function is supposed to turn it into [0, 2, 4]. Here’s the code:
```python
from typing import List

def double_preceding(values: List[float]) -> None:
    """Replace each item in the list with twice the value of the
    preceding item, and replace the first item with 0.

    >>> L = [1, 2, 3]
    >>> double_preceding(L)
    >>> L
    [0, 2, 4]
    """


    if values != []:
        temp = values[0]
        values[0] = 0
        for i in range(1, len(values)):
            values[i] = 2 * temp
            temp = values[i]

Although the example test passes, this code contains a bug. Write a set of unittest tests to identify the bug. Explain what the bug in this function is, and fix it.
```

### Answer :
```python
import unittest
import solution 

class TestDoublePreceeding(unittest.TestCase):
    def test_double_preceeding(self):
        argument = [10, 10, 10]
        expected = [0, 20, 20]
        solution.double_preceding(argument)
        self.assertEqual(argument,expected,"Reoccuring items in list")

unittest.main()
```
