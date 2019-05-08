### Write a function called dict_intersect that takes two dictionaries as arguments and returns a dictionary that contains only the key/value pairs found in both of the original dictionaries.

```python

def dict_intersect(inDict, inDict1) -> dict :

    return dict(inDict.items() & inDict1.items())



# How to use it :

Dictionary0 = {'one' : 1, 'two' : 2 }
Dictionary1 = {'one' : 1, 'three' : 2 }

print(dict_intersect(Dictionary0,Dictionary1))

```