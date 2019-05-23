### All three versions of linear search start at index 0. Rewrite all to search from the end of the list instead of from the beginning. Make sure you test them.

- Linear Search :
    ```python

    from typing import Any

    def linear_search(lst: list, value: Any) -> int:
        i = 0
    
        while i != len(lst) and lst[i] != value:
            i = i + 1
        
        if i == len(lst):
            return -1
        else:
            return i

    ```
- Answer : 

    ```python

    from typing import Any

    def linear_search(lst: list, value: Any) -> int:
        i = len(lst) -1
    
        while i != -1 and lst[i] != value:
            i = i - 1
        
        if i == -1:
            return -1
        else:
            return i

    ```
    