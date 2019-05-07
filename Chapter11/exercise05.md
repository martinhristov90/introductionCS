### The keys in a dictionary are guaranteed to be unique, but the values are not. Write a function called count_values that takes a single dictionary as an argument and returns the number of distinct values it contains. Given the input {’red’: 1, ’green’: 1, ’blue’: 2}, for example, it should return 2.

```python

from typing import Dict

def count_values(inDict: Dict) -> int:

    finalList = []

    for i in inDict.values():
        if i not in finalList:
            finalList.append(i)
    
    return len(finalList)



testDict = {'red':1,'green':1,'blue':2}

#How to use it:

print(count_values(testDict))

```