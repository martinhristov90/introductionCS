### Using unittest, write the five most informative tests you can think of for a function called is_sorted in a module called TestSorting.py that takes a list of integers as input and returns True if they are sorted in nondecreasing order (as opposed to strictly increasing order, because of the possibility of duplicate values), and False otherwise.

### Answer :
```python
import unittest

def is_sorted(inputList: int) -> bool:
    
    # Coping the input list into working copy.
    _copyLst = inputList[:]
    # Sorting the working copy.
    _copyLst = sorted(_copyLst)
    # Testing if the working copy is identical with the input list.
    if _copyLst == inputList :
        return True
    else : 
        return False

class TestIfSorted(unittest.TestCase):
    def testingEmptyList(self):
        argument = is_sorted([])
        expected = True
        self.assertEquals(argument,expected,"Testing empty list")

    def oneEntryList(self):
        argument = is_sorted([2])
        expected = True
        self.assertEquals(argument,expected,"Testing one entry list")

    def testNegativeEntriesSorted(self):
        argument = is_sorted([-3,-2,-1])
        expected = True
        self.assertEquals(argument,expected,"Testing list of negative entries,sorted already")

    def testNegativeEntriesNotSorted(self):
        argument = is_sorted([-2,-1,-3])
        expected = False
        self.assertEquals(argument,expected,"Testing list of negative entries,not sorted")

    def testPositiveentriesSorted(self):
        argument = is_sorted([1,2,3])
        expected = True
        self.assertEquals(argument,expected,"Testing list of positive entries, sorted already")
        
    def testPositiveentriesNotSorted(self):
        argument = is_sorted([2,1,3])
        expected = False
        self.assertEquals(argument,expected,"Testing list of positive entries, not sorted")
    
    def testDoubleEntrie(self):
        argument = is_sorted([1,2,3,3,3])
        expected = True
        self.assertEquals(argument,expected,"Testing list of reoccuring entries, sorted")

unittest.main()
```