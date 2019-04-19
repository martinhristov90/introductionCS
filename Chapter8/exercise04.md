### Variable ids refers to the list [4353, 2314, 2956, 3382, 9362, 3900]. Using list methods, do the following:


- Remove 3382 from the list.
    ```python
    ids = [4353, 2314, 2956, 3382, 9362, 3900]
    >>> ids.remove(3382)
    >>> ids
    [4353, 2314, 2956, 9362, 3900]
    >>> 
    ```
- Get the index of 9362.
    ```python
    >>> ids.index(9362)
    3
    >>> 
    ```
- Insert 4499 in the list after 9362.
    ```python
    >>> ids.insert(3+1,4499)
    >>> ids
    [4353, 2314, 2956, 9362, 4499, 3900]
    >>> 
    ```
- Extend the list by adding [5566, 1830] to it.
    ```python
    >>> ids.append(5566)
    >>> ids.append(1830)
    >>> ids
    [4353, 2314, 2956, 9362, 4499, 3900, 5566, 1830]
    >>> 
    ```
- Reverse the list.
    ```python
    >>> ids
    [1830, 5566, 3900, 4499, 9362, 2956, 2314, 4353]
    >>> 
    ```
- Sort the list.    
    ```python
        >>> ids.sort()
        >>> ids
        [1830, 2314, 2956, 3900, 4353, 4499, 5566, 9362]
        >>> 
    ```