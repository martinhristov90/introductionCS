### Write a function called count_duplicates that takes a dictionary as an argument and returns the number of values that appear two or more times.

```python

from typing import Dict

def count_duplicates(inDict) -> int:

    lstAllValues = []
    lstAdditional = []
    lstFinal = []

    for i in inDict.values():
        lstAllValues.append(i)
        lstAdditional.append(i)
    
    lstFinal = set(lstAllValues).intersection(lstAdditional)

    return(len(lstAllValues) - len(lstFinal))

# How to use it :

testDict = {'one' : 1, 'two' : 2, 'two1' : 2, 'three1' : 3,'three' : 3}

print(count_duplicates(testDict))

```