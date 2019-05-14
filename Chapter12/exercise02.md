### In this exercise, you’ll develop a function that finds the minimum or maximum value in a list, depending on the caller’s request.

- Write a loop (including initialization) to find both the minimum value in a list and that value’s index in one pass through the list.
    ```python

    from typing import List

    def smallestInList(inLst: List) -> int :
        min = inLst[0]
        for i in inLst:
            if i < min:
                min = i
        return min

    # How to use it:

    print(smallestInList([25,3,45,56]))

    ```

- Write a function named min_index that takes one parameter (a list) and returns a tuple containing the minimum value in the list and that value’s index in the list.

    ```python

    from typing import List

    def smallestInListAndIndex(inLst: List) -> int :
        min = inLst[0]
        for i in inLst:
            if i < min:
                min = i
        return (min,inLst.index(min))

    print(smallestInListAndIndex([25,3,45,56]))

    ```

- You might also want to find the maximum value and its index. Write a function named min_or_max_index that has two parameters: a list and a bool. If the Boolean parameter refers to True, the function returns a tuple containing the minimum and its index; if it refers to False, it returns a tuple containing the maximum and its index.

    ```python

    from typing import List

    def min_or_max_index(inLst : List,minOrMax : bool) -> tuple:

        if minOrMax:
            min = inLst[0]
            for i in inLst:
                if i < min:
                    min = i
            return (min,inLst.index(min))

        if not minOrMax:
            max = inLst[0]
            for i in inLst:
                if i > max:
                    max = i
            return (max,inLst.index(max))

    # How to use it:

    print(min_or_max_index([25,3,45,56],False))
    
    ```