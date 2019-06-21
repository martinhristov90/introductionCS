### Using unittest, write four tests for a function called all_prefixes in a module called TestPrefixes.py that takes a string as its input and returns the set of all nonempty substrings that start with the first character. For example, given the string "lead" as input, all_prefixes would return the set {"l", "le", "lea", "lead"}.

### Answer :
```python
import unittest

def all_prefixes(text: str):

    returnSet = []

    if len(text) == 0:
        return set()

    firstLetter = text[0]
    # Coping the input to a working copy.
    
    copyTxt = text
    # Appending to returnSet, all prefixes that start with the first letter at the first possition of the world.
    for i in range(0,len(text)):

        returnSet.append(text[  : i + 1])

    # Looking for second occupance of the first letter of the word.
    nextOccur = copyTxt.find(firstLetter,1)
    # Not going to go inside the loop if not occupancy found, str.find() returns -1 if no occupancy found.
    while nextOccur != -1 :

        for j in range(nextOccur,len(copyTxt)):

            returnSet.append(copyTxt[nextOccur  : j + 1])

        # Cutting the text on letter to the right, after the second occupance.
        copyTxt = copyTxt[nextOccur + 1 :]
        # Finding next occupance.
        nextOccur = copyTxt.find(firstLetter)
        
    return set(returnSet)

class TestAllPrefixes(unittest.TestCase):
    """Tests for all_prefixes."""
    def test_empty(self):
        """Test the empty string."""
        argument = all_prefixes('')
        expected = set()
        self.assertEqual(expected, argument, 'Argument is empty string.')
    def test_single_letter(self):
        """Test a one-character string."""
        argument = all_prefixes('x')
        expected = {'x'}
        self.assertEqual(expected, argument, 'Argument is single letter.')
    def test_word(self):
        """Test a word with unique letters."""
        argument = all_prefixes('lead')
        expected = {'lead', 'l', 'le', 'lea',}
        self.assertEqual(expected, argument, 'Argument is word with unique letters.')
    def test_multiple(self):
        """Test a word with multiple occurences of the first letter."""
        argument = all_prefixes('puppet')
        expected = {'p', 'pu', 'pup', 'pupp', 'puppe', 'puppet', 'pp', 'ppe','ppet', 'pe', 'pet'}
        self.assertEqual(expected, argument, 'First letter occurs multiple times')

unittest.main()
```