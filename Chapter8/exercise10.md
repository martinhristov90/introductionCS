### Variable units refers to the nested list [['km', 'miles', 'league'], ['kg', 'pound', 'stone']]. 
### Using units and either slicing or indexing with positive indices, write expressions that produce the following:


- The first item of units (the first inner list)
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][0]
    ['km', 'miles', 'league']
    >>> 
    ```
- The last item of units (the last inner list)
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][-1:]
    [['kg', 'pound', 'stone']]
    >>> 
    ```
- The string 'km'
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][0][0]
    'km'
    >>> 
    ```
- The string 'kg'
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][1][0]
    'kg'
    >>> 
    ```
- The list ['miles', 'league']
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][0][1:]
    ['miles', 'league']
    >>> 
    ```
- The list ['kg', 'pound']  
    ```python
    >>> [['km', 'miles', 'league'], ['kg', 'pound', 'stone']][1][:-1]
    ['kg', 'pound']
    >>> 
    ```