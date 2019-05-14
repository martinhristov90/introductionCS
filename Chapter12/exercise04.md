### Write a set of doctests for the find-two-smallest functions. Think about what kinds of data are interesting, long lists or short lists, and what order the items are in. Here is one list to test with: [1, 2]. What other interesting ones are there?

```python
    import doctest
    
    def find_two_smallest (inList) :
        """
        (list) -> tuple
        Returns the two smallest numbers in the list passed as argument to the funciton.
        >>> find_two_smallest([5,6,33,4,5,6])
        (4, 5)
        """
        return(sorted(inList)[0],sorted(inList)[1]) 
    
    doctest.testmod()
    print(find_two_smallest([1,2]))
    # Result : (1, 2)
    print(find_two_smallest([0,0]))
    # Result: (0,0)
    print(find_two_smallest([1,1]))
    # Result: (1,1)
```
