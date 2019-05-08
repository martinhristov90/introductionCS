### A balanced color is one whose red, green, and blue values add up to 1.0. Write a function called is_balanced that takes a dictionary whose keys are ’R’, ’G’, and ’B’ and whose values are between 0 and 1 as input and that returns True if they represent a balanced color.

```python

from typing import Dict

def is_balanced (inDict:[str, float]) -> bool:
    
    sumVar = 0.0

    for i in inDict.values():
        sumVar = sumVar + i 

    return sumVar == 1

# How to use it : 

testDict = {'R' : 0.2 , 'G' : 0.2, 'B' : 0.6}

print(is_balanced(testDict))

```