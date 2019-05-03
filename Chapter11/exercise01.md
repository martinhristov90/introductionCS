### Write a function called find_dups that takes a list of integers as its input argument and returns a set of those integers occurring two or more times in the list.

```python

from typing import List,Set

def find_dups(lst: List[int]) -> Set[int]:

    elem_set = set()
    dups_set = set()

    for i in lst:
        len_inital = len(elem_set)
        elem_set.add(i)
        len_after = len(elem_set)
        if len_inital == len_after:
            dups_set.add(i)
    
    return(dups_set)

print(find_dups([1,2,2,2,3]))

```