### Using string method find, write a single expression that produces the index of the second occurrence of o in ’tomato’. 
### Hint: Call find twice.

```python
'tomato'.find('o','tomato'.find('o') + 1 )
5
>>> 
```

### Function definition :

```python
Help on method_descriptor:

find(...)
    S.find(sub[, start[, end]]) -> int
    
    Return the lowest index in S where substring sub is found,
    such that sub is contained within S[start:end].  Optional
    arguments start and end are interpreted as in slice notation.
    
    Return -1 on failure.
>>> 
```