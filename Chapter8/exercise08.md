### Complete the examples in the docstring and then write the body of the following function:

```python
def is_longer(L1: list, L2: list) -> bool:

    """Return True if and only if the length of L1 is longer than the length​
    of L2.​
    >>> is_longer([1, 2, 3], [4, 5])​
    True​
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])​
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3]​
    """​
    if L1.__len__ > L2.__len__:
        return True
    else:
        exit

```